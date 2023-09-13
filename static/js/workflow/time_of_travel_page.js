var baseUrl = "hms/rest/api/v3/workflow/timeoftravel/";
var counter = 100;
var jobID = null;

var startCOMID = null;
var endCOMID = null;
var startLayer = null;
var endLayer = null;
var networkLayer = null;

var lat = null;
var lng = null;

var table = null;
var data = null;
var tableData = null;

var selectedRow = null;
var selectedCol = null;

var totGraphData = [];
var timeWhenTrue = [];
var catchmentArray = [];
var smallDateList = [];
var contaminateList = [];

let geoJSONCatchList = [];
let geoJSONFlowList = [];
let CONTAMINANT_LAYER = null;
let MAP = null;
let smallDateStrings = [];
let LAYER_OPTIONS = null;

let sDate = null;
let eDate = null;
let sHour = null;
let eHour = null;

let dateList = [];

let highestLat = 0;
let lowestLat = 0;
let highestLon = 0;
let lowestLon = 0;
/*var catchmentMap = null;
var catchmentMapList = {};
var catchmentData = null;
var geoGroup = null;
var selectedCatchment = null;
*/

// overrides getData() in general page
function getData() {
    var params = getParameters();
    console.log("time of travel page getData() parameters: ", params);

    localStorage.setItem("tot-params", JSON.stringify(params));

    var requestUrl = window.location.origin + "/" + baseUrl;
    $.ajax({
        type: "POST",
        url: requestUrl,
        accepts: "application/json",
        data: JSON.stringify(params),
        processData: false,
        timeout: 0,
        contentType: "application/json",
        success: function (data, textStatus, jqXHR) {
            console.log("time of travel getData POST response: ", data);
            taskID = data.job_id;
            const model = $("#model_name").html();
            const submodule = $("#submodule_name").html();
            window.location.href = "/hms/" + model + "/" + submodule + "/output_data/" + taskID + "/";

            //setDataRequestCookie(taskID);
            //console.log("Data request success. Task ID: " + taskID);
            //toggleLoader(false, "Processing data request. Task ID: " + taskID);
            //setTimeout(getDataPolling, 5000);
            //$('#component_tabs').tabs("enable", 2);
            //$('#component_tabs').tabs("option", "active", 2);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log("Data request error...");
            console.log(errorThrown);
            // toggleLoader(true, "");
        },
        complete: function (jqXHR, textStatus) {
            console.log("Data request complete");
        },
    });
}

function getParameters() {
    return {
        startCOMID: document.getElementById("id_startCOMID").value,
        endCOMID: document.getElementById("id_endCOMID").value,
        startDate: document.getElementById("id_startDate").value,
        startHour: document.getElementById("id_startHour").value,
        inflowSource: document.getElementById("id_inflowSource").value,
    };
}

$(function () {
    createInputTable();
    setTableData(true);

    $("#id_inflowSource").on("change", function (event, ui) {
        if ($(this).val() === "Input Table") {
            $("#input_datatable").show();
        } else {
            $("#input_datatable").hide();
        }
    });

    $("#open_table_button").on("click", function (event, ui) {
        $("#input_datatable_inner").show();
        $("#backdrop").show();
        $("#open_table_button").hide();
    });
    $("#backdrop_exit").on("click", function (event, ui) {
        $("#input_datatable_inner").hide();
        $("#backdrop").hide();
        $("#open_table_button").show();
    });
    $("#id_startDate").on("change", function (event, ui) {
        setTableData(false);
    });
    $("#id_endDate").on("change", function (event, ui) {
        setTableData(false);
    });
    $("#id_startHour").on("change", function (event, ui) {
        setTableData(false);
    });
    $("#id_endHour").on("change", function (event, ui) {
        setTableData(false);
    });

    $("#input_datatable_inner").on("click", "td", function (e) {
        var selection = table.getSelection();
        if (selection.length === 0) {
            return;
        }
        var cell = e.target;
        selectedRow = selection[0].row;
        selectedCol = cell.cellIndex;
        var v = this.innerHTML;
        if (!v.includes("<input") && $(this).index() === 2) {
            this.innerHTML =
                "<input id='tblCell' class='tblCellEdit' onfocus='this.value = this.value;' type='text' value='" +
                v +
                "'/>";
            document.getElementById("tblCell").focus();
        }
    });
    //
    $("#input_datatable_inner").on("blur", "td", function (e) {
        var v = Number(this.childNodes[0].value);
        this.innerHTML = v;
        tableData[selectedRow][selectedCol] = v;
        drawTable();
        selectedRow = null;
        selectedCol = null;
    });
});

function addZero(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

function setTableData(initial) {
    // console.log("Setting DataTable values");
    var startDate = new Date($("#id_startDate").val());
    startDate.setHours(Number($("#id_startHour").val()));

    var endDate = new Date($("#id_endDate").val());
    endDate.setHours(Number($("#id_endHour").val()));

    var timesteps = [];
    var currentDate = startDate;
    while (currentDate.getTime() < endDate.getTime()) {
        var date = currentDate.getFullYear() + "-" + (currentDate.getMonth() + 1) + "-" + currentDate.getDate();
        var hour = currentDate.getHours();
        var timestep = [date, hour, 0];
        timesteps.push(timestep);
        currentDate.setHours(currentDate.getHours() + 1);
    }
    tableData = timesteps;
    if (!initial) {
        drawTable();
    }
}

function createInputTable() {
    // console.log("Creating input table.");
    var input_table = $("#input_datatable");
    var timeSeriesTableRow = document.createElement("div");
    timeSeriesTableRow.classList.add("input_table_row");
    var openTableButton = document.createElement("input");
    openTableButton.classList.add("open_table");
    openTableButton.id = "open_table_button";
    openTableButton.value = "Open Input Table";
    $(timeSeriesTableRow).append(openTableButton);
    $(input_table).append(timeSeriesTableRow);

    var backdrop = document.createElement("div");
    backdrop.id = "backdrop";
    var backdropExit = document.createElement("div");
    backdropExit.id = "backdrop_exit";
    backdropExit.innerHTML = "x";
    $(backdrop).append(backdropExit);
    $("#input_datatable_top").append(backdrop);
    $("#backdrop").hide();
    $("#input_datatable_inner").hide();
    $("#input_datatable").hide();
}

// Load the Visualization API and specified packages.
google.charts.load("current", { packages: ["table", "corechart"] });

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawTable);

/*Original drawTable function before being restructured

function drawTable(){
    data = new google.visualization.DataTable();
    data.addColumn('string', 'Date');
    data.addColumn('number', 'Hour');
    data.addColumn('number', 'Contaminant Inflow');
    data.addRows(totGraphData);

    table = new google.visualization.Table(document.getElementById('output_data'));
    table.draw(data, {showRowNumber: false, width: '100%', height: '100%', sort: 'disable', page: 'enable', pageSize: 18});
}*/

function drawTable() {
    //Sets title of chart
    const outtitle = document.getElementById("output_dattitle");
    outtitle.innerHTML = "Time of Travel";

    //Defines table and creates first column
    data = new google.visualization.DataTable();
    data.addColumn("string", "Length(km)");
    data.addColumn("string", "ComID");

    //Used to create more columns depending on how many date values there are containing data
    let firstDate = true;
    let timecount = 0;
    for (let x of smallDateList) {
        let dt = (x + "").split(" ");
        let hr = dt[4].split(":");

        let dateString = null;

        //A string used to hold the value of the date as a String in a certain format
        dateString = dt[1] + " " + dt[2] + ", " + dt[3] + "  " + hr[0] + ":00";
        if (firstDate) {
            //Creates an HTML element below the chart title that displays the date value the data begins at
            var outdate = document.createElement("h4");
            outtitle.appendChild(outdate);

            outdate.setAttribute("id", "output_date_title");
            outdate.setAttribute("class", "output_date_title");

            var datetext = document.createTextNode("T starts at: " + dateString + " GMT");
            outdate.appendChild(datetext);

            //Adds first column of T+ counter from starting date with hover capabilities
            data.addColumn("string", '<span class="hovertext" title="' + dateString + '">T+' + timecount + "</span>");
            firstDate = false;
        } else {
            //Adds remaining columns of T+ counters from starting date with hover capabilities
            data.addColumn("string", '<span class="hovertext" title="' + dateString + '">T+' + timecount + "</span>");
        }
        timecount = timecount + 1;
    }

    //Populated the table with data
    for (let ar of contaminateList) {
        data.addRows([ar]);
    }

    //identifies element table will be created at and creates the table with specific settings
    table = new google.visualization.Table(document.getElementById("output_chart"));
    table.draw(data, {
        showRowNumber: false,
        width: "100%",
        height: "100%",
        sort: "disable",
        page: "enable",
        pageSize: 18,
        allowHtml: true,
    });

    //Applies function to all of catchment hyperlinks in the table
    for (let ar of totGraphData) {
        let newLink = document.getElementById(ar[0]);

        //Connects links to draw a table for the individual catchment when clicked
        newLink.onclick = function () {
            catchmentArray = ar;
            drawCatchment();
            return false;
        };
    }
}

//Creates callback for catchment tables
google.charts.setOnLoadCallback(drawCatchment);

//Draws a table for individual catchments
function drawCatchment() {
    //Sets title of chart
    const outtitle = document.getElementById("output_dattitle");
    outtitle.innerHTML = "Time of Travel Data for Catchment: " + catchmentArray[0];

    //Defines chart and creats chart columns
    data = new google.visualization.DataTable();
    data.addColumn("string", "Date & Time");
    data.addColumn("number", "Velocity(m/s)");
    data.addColumn("number", "Flow (m^3/s)");
    data.addColumn("string", "Contaminated");

    //Populates the table with data
    for (let ar of catchmentArray) {
        if (ar != catchmentArray[0]) {
            data.addRows([ar]);
        }
    }

    //Identifies element where table will be created and creates the table with specific settings
    table = new google.visualization.Table(document.getElementById("output_chart"));
    table.draw(data, {
        showRowNumber: false,
        width: "100%",
        height: "100%",
        sort: "disable",
        page: "enable",
        pageSize: 18,
        allowHtml: true,
    });

    //Creates a hyperlink to go back to the true/false table that contains links to all catchments
    var backLink = document.createElement("a");
    var backText = document.createTextNode("Back");
    backLink.appendChild(backText);
    backLink.setAttribute("id", "Back");
    backLink.setAttribute("href", "Back");

    let element = document.getElementById("output_chart");
    element.appendChild(backLink);

    //Adds function to link to redraw the original table
    backLink.onclick = function () {
        drawTable();

        return false;
    };
}

function dataToCSV() {
    return google.visualization.dataTableToCsv(data);
}

function setOutputUI() {
    //Called by pageSpecificLoad and multiple functions in general_page.js
    tableData = getComponentData();

    setMetadata();
    setTotOutputTable();
    setToTOutputMap();
    setTimeout(passContam, 500);
}

function setTotOutputTable() {
    //pulls JSON from specific location
    //$.getJSON('../../../static/json/time_of_travel_nwm.json', (tableData) => {
    var dataTitle = tableData.dataset;
    var sourceTitle = tableData.dataSource;

    //Makes an array dateList to contain all date objects within the JSON.
    //Also pushes to smallDateList to contain each date only once
    dateList = [];
    for (let catchment of Object.keys(tableData.data)) {
        let dates = Object.keys(tableData.data[catchment]);
        for (let date of dates) {
            let dt = date.split(" ");
            let d = dt[0].split("-");
            if (dt.length === 2) {
                let hr = dt[1].split(":");
                if (hr.length === 2) {
                    dateObject = new Date(d[0], d[1] - 1, d[2], hr[0], hr[1], 0, 0);
                } else {
                    dateObject = new Date(d[0], d[1] - 1, d[2], dt[1], 0, 0, 0);
                }
            } else {
                dateObject = new Date(d[0], d[1] - 1, d[2], 0, 0, 0);
            }

            //Adds elements to global array smallDateList to contain each date only once
            if (smallDateList.length === 0) {
                smallDateList.push(dateObject + " ");
            } else {
                let sameCheck = true;
                for (let element of smallDateList) {
                    if (element === dateObject + " ") {
                        sameCheck = false;
                    }
                }
                if (sameCheck) {
                    smallDateList.push(dateObject + " ");
                }
            }

            dateList.push(dateObject);
        }
    }

    //console.log(dateList);
    earlyTimeToT();

    //Loop used to sort through the JSON and pull out all of the data
    let velAndLen = [];
    //console.log("TempCatchData:", tableData.data);
    for (let catchment of Object.keys(tableData.data)) {
        catchmentArray = []; //resetting the global value
        let catchEntries = Object.entries(tableData.data[catchment]);
        //console.log("Test Data", catchEntries);

        let dateCounter = 0;
        let comIDLogged = true;
        for (let element of catchEntries) {
            let entry = element[1];

            //used to help sort through the date and time from within the data
            let dt = (dateList[dateCounter] + "").split(" ");
            let hr = dt[4].split(":");

            //Makes sure only the first element of a list is the com id
            if (comIDLogged) {
                catchmentArray.push(entry[0]);
                comIDLogged = false;
            }

            //Pushes the data as a whole into a more organized array of the catchment's data
            let tempDataArray = [
                dt[1] + " " + dt[2] + ", " + dt[3] + "  " + hr[0] + ":00",
                parseFloat(entry[2]),
                parseFloat(entry[3]),
                entry[4],
            ];

            catchmentArray.push(tempDataArray);

            velAndLen.push([entry[0], parseFloat(entry[1]), parseFloat(entry[2])]);

            dateCounter = dateCounter + 1;
        }

        //pushes collected catchment information into arrays
        totGraphData.push(catchmentArray);
    }

    //This block of code is used to sort data to be in the same order as the catchments listed in the metadata
    let catchments = tableData.metadata.catchments.split(",");
    let tempDataList = [];
    let tempVL = [];
    for (let element of catchments) {
        for (let dataElement of totGraphData) {
            //sorts totGraphData according to metadata
            if (element === dataElement[0]) {
                tempDataList.push(dataElement);
            }
        }
        for (let vLement of velAndLen) {
            //sorts velAndLen according to metadata
            if (element === vLement[0]) {
                tempVL.push(vLement);
            }
        }
    }

    //sets the arrays to sorted values
    velAndLen = tempVL;
    totGraphData = tempDataList;

    let whenContam = []; //An array used to store when catchments first become contaminated
    let ind = 0; //used to keep track of which catchment is being measured
    let prevInd = -1; //used to keep track of the previous catchment mesaured so some process are not repeated twice
    let timeFrac = 0; //the fraction of time remaining in the hour that the contamination spreads to the next catchment
    let lengt = 0; //used to track the current addidtive length and compare it to the catchment's length

    //This loop calculates the correct hour in which the catchments first become contaminated
    for (let hour = 0; hour < 18 && ind < totGraphData.length; hour++) {
        let tempCat = totGraphData[ind]; //grabs the catchment
        let templev = velAndLen[ind * 18 + hour]; //grabs the velocity and length for the catchment at the specific hour
        let distTravel = 0;

        //pushes data of when a catchment first becomes contaminated to an array
        if (prevInd != ind) {
            whenContam.push([
                tempCat[0],
                tempCat[hour + 1][0],
                tempCat[hour + 1][1],
                tempCat[hour + 1][2],
                tempCat[hour + 1][3],
            ]);
            prevInd = ind;
        }

        //checks to make sure the current hour is not the same as the previous loop
        if (timeFrac == 0) {
            distTravel = templev[2] * 3.6; //velocity(m/s) is multiplied by 3.6 to see distance traveled in km
            lengt += distTravel; //adds length to track current distance traveled in catchment

            /*if the additive length exceeds the catchment length, a fraction will be taken of the 
                  remaining time in the current hour. index goes to next catchment and length set to 0*/
            if (lengt >= templev[1]) {
                let extraDist = lengt - templev[1];
                //let currentStream = (templev[2]*3.6) - extraDist;
                timeFrac = extraDist / distTravel;
                ind++;
                lengt = 0;
            }
        } else {
            //if there is leftover time in the hour, this will utilize it to ensure the full hour is used
            distTravel = timeFrac * (templev[2] * 3.6); //similar to before, but instead multiplied by the remaining fraction of hour left
            lengt += distTravel;

            /*similar to before, but if the catchment exceeds length again while a time fraction 
                  remains, a new smaller fraction is taken and subtracted from the current one*/
            if (lengt >= templev[1]) {
                let extraDist = lengt - templev[1];
                //let currentStream = (templev[2]*3.6) - extraDist;
                timeFrac = timeFrac - extraDist / distTravel;
                ind++;
                lengt = 0;
            } else {
                //once the full hour is used the fraction is set back to 0
                timeFrac = 0;
            }
        }

        //console.log("Catchment: " + tempCat[0] + ", Stream Length: " + templev[1] + ", Hour: " + hour + ", Velocity: " + templev[2] + ", Length this hour: " + distTravel + ", Time Fraction: " + timeFrac
        // + ", Distance traveled so far: " + lengt);

        //if the time fraction is greater than zero, then the current hour is not finished being measured
        if (timeFrac > 0) {
            hour--;
        }
    }

    //console.log("New Math Test:", whenContam);

    let tempGraphArray = []; //new data for totGraphData
    ind = 0; //used keep track of the index of whenContam
    let dCounter = 0; //keeps track of the date when compared to dateList

    //this loop is utilizes whenContam to correct the True/False data within all of the needed Arrays
    for (let cat of totGraphData) {
        //cycles through catchments
        let tempNewData = []; //new data for for this catchment
        let contaminantInfo = []; //new data for contaminateList
        tempNewData.push(cat[0]);
        let allTruAfter = false; //used to set the rest of a catchment to contaminated once the conditions are met
        for (let c of cat) {
            //cycles through the hourly info in catchments
            //skips the first element of catchment info since it is the catchment number
            if (c != cat[0]) {
                /*Used to check: 
                    the correct catchment is being measured
                    data does no go past the index of whenContam since it not all catchments may be contaminated
                    if the catchment is contaminated at this hour*/
                if (ind < whenContam.length && whenContam[ind][0] == cat[0] && whenContam[ind][1] == c[0]) {
                    //once the catchment is contaminated all hours after it must be as well
                    allTruAfter = true;
                    ind++; //next index of whenContam

                    //pushes corrected data to tempNewData, contaminantInfo, and timeWhenTrue
                    tempNewData.push([c[0], c[1], c[2], "True"]);
                    contaminantInfo.push({ v: "T", f: null, p: { style: "background-color: lightpink;" } });

                    let tempDate = [cat[0], c[0], dateList[dCounter]];
                    timeWhenTrue.push(tempDate);
                } else if (allTruAfter) {
                    //occurs when the catchment is confirmed to be contaminated before the current hour
                    tempNewData.push([c[0], c[1], c[2], "True"]);
                    contaminantInfo.push({ v: "T", f: null, p: { style: "background-color: lightpink;" } });

                    let tempDate = [cat[0], c[0], dateList[dCounter]];
                    timeWhenTrue.push(tempDate);
                } else {
                    //if the catchment is not contaminated yet, the correct data is pushed to tempNewData and contaminantInfo
                    tempNewData.push([c[0], c[1], c[2], "False"]);
                    contaminantInfo.push({ v: "F", f: null, p: { style: "background-color: lightgreen;" } });
                }
                dCounter++;
            } else {
                //this only occurs once per catchment when c is just the catchment number
                //grabs the length of the catchment to insert into the data table
                let dat = totGraphData.indexOf(cat);
                let lDat = velAndLen[dat * 18][1] + "";
                contaminantInfo.push(lDat);

                //inserts a link of the catchment's info
                contaminantInfo.push('<a id="' + cat[0] + '" href="#">' + cat[0] + "</a>");
            }
        }

        //pushes the correct data to contaminateList and tempGraphArray
        contaminateList.push(contaminantInfo);
        tempGraphArray.push(tempNewData);
    }
    //console.log("Velocity And Length:", velAndLen);

    totGraphData = tempGraphArray; //changes totGraphData to have corrected True/False data

    console.log("Contaminated List: ", contaminateList);
    console.log("When Turned True: ", timeWhenTrue);
    console.log("Data: ", totGraphData);

    //creates new html elements to put the chart and titles within output_data rather than changing output_data as a whole
    const outdata = document.getElementById("output_data");

    var outtitle = document.createElement("h3");
    outtitle.setAttribute("id", "output_dattitle");
    outtitle.setAttribute("class", "output_title");

    var outchart = document.createElement("div");
    outchart.setAttribute("id", "output_chart");

    outdata.appendChild(outtitle);
    outdata.appendChild(outchart);

    drawTable(); //calls draw table to create a chart of the data
    //});
}

//Used to create a map of the catchments and visual representation of what was contaminated at what time
function setToTOutputMap() {
    //$.getJSON('../../../static/json/time_of_travel_nwm.json', (tableData) => {

    //Arrange HTML elements to set up a location for the map on the webpage
    const outData = document.getElementById("output_data_block_table");

    let outMapData = document.createElement("div");
    outData.appendChild(outMapData);

    let outMap = document.createElement("div");
    let outMapTitle = document.createElement("h3");
    outMapData.appendChild(outMapTitle);
    outMapData.appendChild(outMap);

    outMapData.setAttribute("id", "output_map_data");

    outMap.setAttribute("id", "output_map");

    outMapTitle.setAttribute("id", "output_map_title");
    outMapTitle.setAttribute("class", "output_title");

    let titleText = document.createTextNode("Time of Travel Map");
    outMapTitle.appendChild(titleText);

    //Used to grab the coordinate data of the catchments and put it into one list
    //https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/Catchments_NP21_Simplified/MapServer/0/query?where=FEATUREID%3D
    //&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=geojson
    /*Test Com IDs:
            6275977 - 6277141
            6277245 - 6277403
            6277159 - 6277401
            6330834 - 6331692
            1052709 - 1050215*/
    let catchment_url_base =
        "https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/Catchments_NP21_Simplified/MapServer/0/query?where=FEATUREID%3D";
    let flowline_url_base =
        "https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/NHDSnapshot_NP21/MapServer/0/query?where=COMID%3D";

    let catchment_url_extension =
        "&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=geojson";
    let flowline_url_extension =
        "&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=geojson";

    let catchments = tableData.metadata.catchments.split(",");
    let geoCoordsList = [];

    //For each com id, arranges query urls and queries them for the geoJSON data as well as geometries
    for (let comid of catchments) {
        let coords = [];
        let catchment_query_url = catchment_url_base + comid + catchment_url_extension;
        let flowline_query_url = flowline_url_base + comid + flowline_url_extension;

        //Query the catchment
        $.ajax({
            async: false,
            type: "GET",
            url: catchment_query_url,
            success: function (data, textStatus, jqXHR) {
                //console.log(data);

                if (Object.entries(data)[1][1][0].geometry.type === "MultiPolygon") {
                    let firstEntries = Object.entries(data)[1][1][0].geometry.coordinates[0][0][0];
                    coords = firstEntries;
                } else {
                    let firstEntries = Object.entries(data)[1][1][0].geometry.coordinates[0][0];
                    coords = firstEntries;
                }

                geoJSONCatchList.push([comid, data]);
            },
        });
        geoCoordsList.push([comid, coords]);

        //Query the flowline
        $.ajax({
            async: false,
            type: "GET",
            url: flowline_query_url,
            success: function (data, textStatus, jqXHR) {
                //console.log(data);

                geoJSONFlowList.push([comid, data]);
            },
        });
    }
    console.log("Geo JSON Catchments: ", geoJSONCatchList);
    console.log("Geo JSON Flowlines: ", geoJSONFlowList);
    console.log("Geo Coords list: ", geoCoordsList);

    highestLat = 0;
    lowestLat = 0;
    highestLon = 0;
    lowestLon = 0;
    let frst = true;

    //Take the average of the coordinate data and use it to center the map around the catchments
    let avgLAT = 0;
    let avgLNG = 0;
    for (let entry of geoCoordsList) {
        avgLAT = avgLAT + entry[1][1];
        avgLNG = avgLNG + entry[1][0];

        if (entry === geoCoordsList[geoCoordsList.length - 1]) {
            avgLAT = avgLAT / geoCoordsList.length;
            avgLNG = avgLNG / geoCoordsList.length;
        }

        if (frst) {
            highestLat = entry[1][1];
            highestLon = entry[1][0];
            lowestLat = entry[1][1];
            lowestLon = entry[1][0];
            frst = false;
        } else {
            if (entry[1][1] > highestLat) {
                highestLat = entry[1][1];
            }
            if (entry[1][1] < lowestLat) {
                lowestLat = entry[1][1];
            }
            if (entry[1][0] > highestLon) {
                highestLat = entry[1][0];
            }
            if (entry[1][0] < lowestLon) {
                lowestLon = entry[1][0];
            }
        }
    }

    console.log("Avergae Lat: " + avgLAT + ", Average Lon: " + avgLNG);

    //Create a slider below the map to allow for date changes
    let sliderContainer = document.createElement("div");
    sliderContainer.setAttribute("class", "slidercontainer");
    sliderContainer.setAttribute("id", "slidercontainer");
    outMapData.appendChild(sliderContainer);

    let dateSlider = document.createElement("input");
    dateSlider.setAttribute("type", "range");
    dateSlider.setAttribute("min", "0");
    dateSlider.setAttribute("max", smallDateList.length - 1 + "");
    dateSlider.setAttribute("value", "0");
    dateSlider.setAttribute("class", "slider");
    dateSlider.setAttribute("id", "dateSlider");
    sliderContainer.appendChild(dateSlider);

    //Create date text below the slider to identify which date the user is viewing
    let slideDateDisplay = document.createElement("h4");
    slideDateDisplay.setAttribute("id", "sliderDate");
    outMapData.appendChild(slideDateDisplay);

    //Makes an String array of the available dates for easier use
    smallDateStrings = [];
    for (let element of smallDateList) {
        let dt = (element + "").split(" ");
        let hr = dt[4].split(":");

        let dateString = null;

        dateString = dt[1] + " " + dt[2] + ", " + dt[3] + "  " + hr[0] + ":00";
        smallDateStrings.push(dateString);
    }
    slideDateDisplay.innerHTML = smallDateStrings[0];

    createMap(avgLAT, avgLNG);

    let buttonPressed = false;

    //Makes slider display the correct date
    dateSlider.oninput = function () {
        slideDateDisplay.innerHTML = smallDateStrings[this.value];
        dateSlider.setAttribute("value", this.value + "");
        makeContaminateLayer(false);

        if (buttonPressed == true) {
            buttonPressed = false;
        }

        autoCycleButton.onclick = function () {
            buttonPressed = !buttonPressed;
            console.log("Button Pressed!, ", buttonPressed);
            setTimeout(cycle, 500);
        };
    };

    //Used to create a button that automatically cycles through the dates on the map
    //Currently only able to cycle through if user has not used slider. Unsure what breaks
    let autoCycleButton = document.createElement("button");
    autoCycleButton.setAttribute("class", "autoCycleButton");
    autoCycleButton.setAttribute("id", "autoCycleButton");
    autoCycleButton.innerHTML = "Press to cycle through automatically";
    outMapData.appendChild(autoCycleButton);

    autoCycleButton.onclick = function () {
        buttonPressed = !buttonPressed;
        console.log("Button Pressed!, ", buttonPressed);
        setTimeout(cycle, 500);
    };

    //cycles through if button is pressed
    function cycle() {
        if (buttonPressed == true) {
            let val = parseInt(dateSlider.getAttribute("value")) + 1;

            if (val >= smallDateList.length) {
                dateSlider.setAttribute("value", "0");
                $(".dateSlider").slider("refresh");
                slideDateDisplay.innerHTML = smallDateStrings[dateSlider.value];
                makeContaminateLayer(false);
            } else {
                dateSlider.setAttribute("value", val + "");
                $(".dateSlider").slider("refresh");
                slideDateDisplay.innerHTML = smallDateStrings[dateSlider.value];
                makeContaminateLayer(false);
            }
            console.log("Small Date String: ", smallDateStrings[dateSlider.value]);
            console.log("val: ", val);
            setTimeout(cycle, 500);
        }
        autoCycleButton.onclick = function () {
            buttonPressed = !buttonPressed;
            console.log("Button Pressed!, ", buttonPressed);
            setTimeout(cycle, 500);
        };
    }
    //});
}

function createMap(lat, lon) {
    //Create the map, Jason's code
    const DEFAULT_LAT = lat;
    const DEFAULT_LNG = lon;
    const DEFAULT_ZOOM = 13;

    // catchments
    const URL_NP21_CATCHMENTS =
        "https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/Catchments_NP21_Simplified/MapServer/0";
    // WBD - HUC_8
    const URL_NP21_HUC8 = "https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/WBD_NP21_Simplified/MapServer/2";
    // flowlines
    const URL_NP21_FLOWLINES =
        "https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/NHDSnapshot_NP21/MapServer/0";

    // build base map layer
    MAP = L.map("output_map").setView([DEFAULT_LAT, DEFAULT_LNG], DEFAULT_ZOOM);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(MAP);

    // build map layers
    const CATCHMENTS_LAYER = L.esri
        .featureLayer({
            url: URL_NP21_CATCHMENTS,
        })
        .addTo(MAP);
    CATCHMENTS_LAYER.setStyle({
        color: "orange",
        fillOpacity: 0,
    });

    const BOUNDARIES_LAYER = L.esri
        .featureLayer({
            url: URL_NP21_HUC8,
        })
        .addTo(MAP);
    BOUNDARIES_LAYER.setStyle({
        color: "purple",
        fillOpacity: 0,
    });

    const FLOWLINES_LAYER = L.esri
        .featureLayer({
            url: URL_NP21_FLOWLINES,
        })
        .addTo(MAP);

    const OVERLAY_MAPS = {
        "HUC8 Boundaries": BOUNDARIES_LAYER,
        Catchments: CATCHMENTS_LAYER,
        "Flow Lines": FLOWLINES_LAYER,
    };
    LAYER_OPTIONS = L.control.layers(null, OVERLAY_MAPS);
    LAYER_OPTIONS.addTo(MAP);

    //creates a legend for the map
    let LEGEND = L.control({ position: "bottomleft" });

    LEGEND.onAdd = function (MAP) {
        var div = L.DomUtil.create("div", "legend");
        div.setAttribute(
            "style",
            "background: rgba(255,255,255,0.8); box-shadow: 0 0 15px rgba(0,0,0,0.2); border-radius: 5px; float: left; text-align: center; padding: 6px 8px;"
        );
        div.innerHTML += "<h4>Legend</h4>";
        div.innerHTML += "<br>";
        div.innerHTML += '<i style="background: #000000"></i><span>Selected Catchments</span><br>';
        div.innerHTML += '<i style="background: #0000ff"></i><span>Uncontaminated</span><br>';
        div.innerHTML += '<i style="background: #ff0000"></i><span>Contaminated</span><br>';
        div.innerHTML += '<i style="background: #ffa500"></i><span>Catchments</span><br>';
        div.innerHTML += '<i style="background: #3388ff"></i><span>Flow Lines</span><br>';
        div.innerHTML += '<i style="background: #800080"></i><span>HUC8</span><br>';

        return div;
    };

    LEGEND.addTo(MAP);

    /*Click Interactions, currently unused
             // app interaction
             function handleMapClick(e) {
                const LAT_LNG = e.latlng;
                sendMessageToDotnet(
                    `Message from map click lat: ${LAT_LNG.lat}, lng: ${LAT_LNG.lng}`
                );
            }
            MAP.on("click", handleMapClick);
        
            // dotnet <=> js message handlers
            // receive message dotnet
            window.chrome.webview.addEventListener("message", (event) => {
                console.log(`"message" event received from dotnet: `, event);
                const message = event.data;
                if (typeof message === "string")
                    this.document.getElementById("message-bar").innerHTML =
                        event.data;
            });
        
            // send message to dotnet
            function sendMessageToDotnet(message) {
                window.chrome.webview.postMessage(message);
            }
        */
}

//Contaminant layerGroup added with many features
function makeContaminateLayer(firstTime) {
    let contaminateLayerOn = true;
    /*Ensures it is not adding multiple of the same layer or overlay. 
    Also helps to check whether layer is turned off in overlay options*/
    if (firstTime != true) {
        if (MAP.hasLayer(CONTAMINANT_LAYER)) {
            MAP.removeLayer(CONTAMINANT_LAYER);
            //console.log("Layer is on!");
        } else {
            contaminateLayerOn = false;
            //console.log("Layer is off!");
        }
        LAYER_OPTIONS.removeLayer(CONTAMINANT_LAYER);
    }

    let dateSlider = document.getElementById("dateSlider");

    /*Checks the Com IDs and the Dates to compare the time a catchment was first contaminated to 
    the current set time on the slider*/
    CONTAMINANT_LAYER = L.layerGroup();
    for (let element of geoJSONCatchList) {
        //Creates a new feature using the JSON
        let newFeature = L.geoJSON(element[1]).addTo(CONTAMINANT_LAYER);

        newFeature.setStyle({
            color: "black",
            fillOpacity: 0.1,
        });
    }
    for (let element of geoJSONFlowList) {
        //Creates a new feature using the JSON
        let newFeature = L.geoJSON(element[1]).addTo(CONTAMINANT_LAYER);
        //Loops through times when catchments were first contaminated
        const contaminateCatchment = timeWhenTrue.find((catchment) => {
            return catchment[0] === element[0];
        });
        //Checks Com ID to ensure the correct geometry is changing color
        if (contaminateCatchment && contaminateCatchment[1] <= smallDateStrings[dateSlider.value]) {
            //If Catchment is contaminated at current time, it will appear red
            newFeature.setStyle({
                color: "red",
            });
        } else {
            newFeature.setStyle({
                color: "blue",
            });
        }
    }
    //Checks to see if the layer should be re-added to the map
    if (contaminateLayerOn) {
        CONTAMINANT_LAYER.addTo(MAP);
    }

    /*Creates overlay option to add or remove the layer. Also allows user to 
    reenable the layer with the correct data, even if the date has changed*/
    LAYER_OPTIONS.addOverlay(CONTAMINANT_LAYER, "Selected Catchments");
}

//Passes function without parameters used for setTimeout functions
function passContam() {
    makeContaminateLayer(true);
}

function earlyTimeToT() {
    sDateList = localStorage.getItem("startDate").split("-");
    //eDateList = localStorage.getItem('endDate').split('-');
    sHour = localStorage.getItem("startHour");
    //eHour = localStorage.getItem('endHour');

    if (sDateList[1] < 10) {
        sDateList[1] = "0" + sDateList[1];
    }

    if (sDateList[2] < 10) {
        sDateList[2] = "0" + sDateList[1];
    }

    sDate = new Date(sDateList[0], sDateList[1] - 1, sDateList[2], sHour + 4, 0, 0);
    console.log(sDate);

    //eDate = new Date(eDateList[0], eDateList[1] - 1, eDateList[2], eHour + 4, 0, 0);
    //console.log(eDate);

    /*if(true){
        let ncUrl = 'https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/nwm.' + sDateList[0] + sDateList[1] + sDateList[2] + '/short_range/nwm.t' + '' + 'z.short_range.channel_rt.f0' + '' + '.conus.nc';

        //let currentHour = sHour + 4;
        let currentHour = today.getHours();
        console.log(currentHour);

        const fetch = require('node-fetch');
        const NetCDFReader = require('netcdfjs');

        let array = [];

        let f = 1;
        let t = 0;
        while(f < 19){
            let tempF = f;
            let tempT = t;
            if(f < 10){
                tempf = '0' + f;
            }
            if(t < currentHour){
                if(t > 23){
                    t = '0';
                    sDateList[2] = sDateList[2].parseInt() + 1;
                    if(sDateList[2] < 10){
                        sDateList[2] = '0' + sDateList[2];
                    }
                }
                if(t < 10){
                    tempT = '0' + t;
                }
            }
            ncUrl = 'https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/nwm.' + sDateList[0] + sDateList[1] + sDateList[2] + '/short_range/nwm.t' + tempT + 'z.short_range.channel_rt.f0' + tempF + '.conus.nc';
            fetch(ncUrl)
            .then(response => response.arrayBuffer())
            .then(arrayBuffer => {
                const reader = new NetCDFReader(arrayBuffer);
                const jsonData = reader.getDataVariable('6275977')

                console.log(jsonData)
            })
            
            f += 1;
            t += 1;
        }
    }*/
}

// // -------------- MAP code -------------- //
// // initialize the map
// //var map = L.map('map', {renderer: L.svg({padding: 100})}).setView([33.926250, -83.356552], 5);
//
// // load basemap
// var layer = null;
// setBasemap('Imagery');
// addStreams();
// // var layer = L.esri.basemapLayer('Imagery').addTo(map);
// var layerLabels;
//
// function setOutputUI(){
//     //setOutputPage();
//     setMetadata();
//     setDataGraph2();
//     return false;
// }
//
// function setBasemap(basemap) {
//     if (layer) {
//         map.removeLayer(layer);
//     }
//     layer = L.esri.basemapLayer(basemap);
//
//     map.addLayer(layer);
//
//     if (layerLabels) {
//         map.removeLayer(layerLabels);
//     }
//
//     if (basemap === 'ShadedRelief' || basemap === 'Imagery' || basemap === 'Terrain'
//     ) {
//         layerLabels = L.esri.basemapLayer(basemap + 'Labels');
//         map.addLayer(layerLabels);
//     }
// }
//
// function changeBasemap(basemaps) {
//     var basemap = basemaps.value;
//     setBasemap(basemap);
//     addStreams();
// }
//
// // ------------ STREAM NETWORK code ------------- //
//
// function addStreams() {
//     L.tileLayer.wms('https://watersgeo.epa.gov/arcgis/services/NHDPlus_NP21/NHDSnapshot_NP21/MapServer/WmsServer??', {
//         layers: 4,
//         format: 'image/png',
//         minZoom: 0,
//         maxZoom: 18,
//         transparent: true
//     }).addTo(map);
// }
//
// // ------------ STREAM NETWORK INFO code ------------- //
//
// var info = L.control();
//
// info.onAdd = function (map) {
//     this._div = L.DomUtil.create('div', 'stream_info');
//     this.update();
//     return this._div;
// };
// info.update = function (props) {
//     this._div.innerHTML = '<h5>Stream Network Details</h5>' +
//         '<table id="stream_info_table" style="margin-bottom: 0px !important; background: none !important;"> ' +
//         '<tr><td class="startCOMID_color">Start COMID:</td> <td id="startCOMIDVal"></td></tr>' +
//         '<tr><td class="endCOMID_color">End COMID:</td><td id="endCOMIDVal"></td></tr>' +
//         '<tr><td>Network Length:</td><td id="lengthVal"></td></tr>' +
//         '<tr><td>Network Flowtime:</td><td id="flowtimeVal"></td></tr>' +
//         '<tr><td>Total Stream Segments:</td><td id="segmentCount"></td></tr></table>';
// };
// info.addTo(map);

// ------------ Main JS ------------- //
