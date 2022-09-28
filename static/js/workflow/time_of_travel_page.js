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
var baseUrl = 'hms/rest/api/v3/workflow/timeoftravel/';
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

/*var catchmentMap = null;
var catchmentMapList = {};
var catchmentData = null;
var geoGroup = null;
var selectedCatchment = null;
*/

$(function () {
    createInputTable();
    setTableData(true);

    $('#id_inflowSource').on("change", function(event, ui){
        if($(this).val() === "Input Table")
        {
            $("#input_datatable").show();
        }
        else{
            $("#input_datatable").hide();
        }
    });

    $('#open_table_button').on("click", function(event, ui){
       $('#input_datatable_inner').show();
       $('#backdrop').show();
       $("#open_table_button").hide();
    });
    $('#backdrop_exit').on("click", function(event, ui){
        $('#input_datatable_inner').hide();
        $('#backdrop').hide();
        $("#open_table_button").show();
    });
    $('#id_startDate').on("change", function(event, ui){
        setTableData(false);
    });
    $('#id_endDate').on("change", function(event, ui){
        setTableData(false);
    });
    $('#id_startHour').on("change", function(event, ui){
        setTableData(false);
    });
    $('#id_endHour').on("change", function(event, ui){
        setTableData(false);
    });

    $('#input_datatable_inner').on('click', 'td', function (e) {
        var selection = table.getSelection();
        if(selection.length === 0){
            return;
        }
        var cell = e.target;
        selectedRow = selection[0].row;
        selectedCol = cell.cellIndex;
        var v = this.innerHTML;
        if (!v.includes('<input') && $(this).index() === 2) {
            this.innerHTML = "<input id='tblCell' class='tblCellEdit' onfocus='this.value = this.value;' type='text' value='" + v + "'/>";
            document.getElementById('tblCell').focus();
        }
    });
    //
    $('#input_datatable_inner').on('blur', 'td', function (e) {
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

function setTableData(initial){
    // console.log("Setting DataTable values");
    var startDate = new Date($('#id_startDate').val());
    startDate.setHours(Number($('#id_startHour').val()));

    var endDate = new Date($('#id_endDate').val());
    endDate.setHours(Number($('#id_endHour').val()));

    var timesteps = [];
    var currentDate = startDate;
    while (currentDate.getTime() < endDate.getTime()){
        var date = currentDate.getFullYear() + "-" + (currentDate.getMonth()+1) + "-" + currentDate.getDate();
        var hour = currentDate.getHours();
        var timestep = [date, hour, 0];
        timesteps.push(timestep);
        currentDate.setHours(currentDate.getHours() + 1);
    }
    tableData = timesteps;
    if(!initial){
        drawTable();
    }
}

function getParameters(){
    //var timeseries = dataToCSV();
    var requestJson = {
        "csrfmiddlewaretoken": getCookie("csrftoken"),
        "source": null,
        /*"dateTimeSpan": {
            "startDate": $("#id_startDate").val() + " " + $('#id_startHour').val(),
            "endDate": $('#id_endDate').val() + " " + $('#id_endHour').val()
        },*/
        "geometry": {
            "geometryMetadata": {
                "startCOMID": $("#id_startCOMID").val(),
                "endCOMID": $('#id_endCOMID').val()
            }
        },
        "inflowSource": $("#id_inflowSource").val(),
        "contaminantInflow":  null,
        "units": "default",
        "outputFormat": "json"
    };
    console.log("getParam:", requestJson);
    return requestJson;
}

// function getData() {
//     var params = getParameters();
//     var jsonParams = JSON.stringify(params);
//     var requestUrl = window.location.origin + "/" + baseUrl;
//     $.ajax({
//         type: "POST",
//         url: requestUrl,
//         accepts: "application/json",
//         data: jsonParams,
//         processData: false,
//         timeout: 0,
//         contentType: "application/json",
//         success: function (data, textStatus, jqXHR) {
//             jobID = taskID;//data.job_id;
//             console.log("Data request success. Task ID: " + jobID);
//             toggleLoader(false, "Processing data request. Task ID: " + jobID);
//             setTimeout(getDataPolling, 30000);
//             // $('#workflow_tabs').tabs("enable", 2);
//             // $('#workflow_tabs').tabs("option", "active", 2);
//         },
//         error: function (jqXHR, textStatus, errorThrown) {
//             console.log("Data request error...");
//             console.log(errorThrown);
//         },
//         complete: function (jqXHR, textStatus) {
//             console.log("Data request complete");
//         }
//     });
//     return false;
// }

// function getDataPolling() {
//     //counter = counter - 1;
//     var requestUrl = window.location.origin + "/hms/rest/api/v2/hms/data";
//     jobID = taskID;
//     if (counter > 0) {
//         $.ajax({
//             type: "GET",
//             url: requestUrl + "?job_id=" + jobID,
//             accepts: "application/json",
//             timeout: 0,
//             contentType: "application/json",
//             success: function (data, textStatus, jqXHR) {
//                 if (data.status === "SUCCESS") {
//                     if (typeof data.data === "string") {
//                         jobData = JSON.parse(data.data);
//                     }else{
//                         jobData = data.data;
//                     }
//                     setOutputPage();
//                     console.log("Task successfully completed and data was retrieved.");
//                     // dyGraph.resize();
//                     // counter = 25;
//                 }
//                 else if (data.status === "FAILURE") {
//                     toggleLoader(false, "Task " + jobID + " encountered an error.");
//                     console.log("Task failed to complete.");
//                 }
//                 else {
//                     setTimeout(getDataPolling, 10000);
//                 }
//             },
//             error: function (jqXHR, textStatus, errorThrown) {
//                 console.log("Data request error...");
//                 console.log(errorThrown);
//                 toggleLoader(false, "Error retrieving data for task ID: " + jobID);
//             },
//             complete: function (jqXHR, textStatus) {
//                 console.log("Data request complete");
//             }
//         });
//     }
//     else {
//         console.log("Failed to get data, reached polling cap.")
//     }
//     return false;
// }

function createInputTable(){
    // console.log("Creating input table.");
    var input_table = $('#input_datatable');
    var timeSeriesTableRow = document.createElement('div');
    timeSeriesTableRow.classList.add('input_table_row');
    var openTableButton = document.createElement('input');
    openTableButton.classList.add("open_table");
    openTableButton.id = 'open_table_button';
    openTableButton.value = 'Open Input Table';
    $(timeSeriesTableRow).append(openTableButton);
    $(input_table).append(timeSeriesTableRow);

    var backdrop = document.createElement('div');
    backdrop.id = "backdrop";
    var backdropExit = document.createElement('div');
    backdropExit.id = "backdrop_exit";
    backdropExit.innerHTML = "x";
    $(backdrop).append(backdropExit);
    $('#input_datatable_top').append(backdrop);
    $('#backdrop').hide();
    $('#input_datatable_inner').hide();
    $('#input_datatable').hide();
}

// Load the Visualization API and specified packages.
google.charts.load('current', {'packages':['table', 'corechart']});

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

function drawTable(){
    //Sets title of chart
    const outtitle = document.getElementById("output_dattitle");
    outtitle.innerHTML= "Time of Travel";

    //Defines table and creates first column
    data = new google.visualization.DataTable();
    data.addColumn('string', 'ComID');

    //Used to create more columns depending on how many date values there are containing data
    let firstDate = true;
    let timecount = 0;
    for(let x of smallDateList){
        let dt = (x + "").split(" ");
        let hr = dt[4].split(":");

        let dateString = null;

        //A string used to hold the value of the date as a String in a certain format
        dateString = (dt[1] + " " + dt[2] + ", " + dt[3] + "  " + hr[0] + ":00");
        if(firstDate){
            //Creates an HTML element below the chart title that displays the date value the data begins at
            var outdate = document.createElement("h4");
            outtitle.appendChild(outdate);

            outdate.setAttribute('id', 'output_date_title');
            outdate.setAttribute('class', "output_date_title");

            var datetext = document.createTextNode("T starts at: " + dateString);
            outdate.appendChild(datetext);

            //Adds first column of T+ counter from starting date with hover capabilities
            data.addColumn('string', '<span class="hovertext" title="' + dateString + '">T+' + timecount + '</span>');
            firstDate = false;
        }
        else{
            //Adds remaining columns of T+ counters from starting date with hover capabilities
            data.addColumn('string', '<span class="hovertext" title="' + dateString + '">T+' + timecount + '</span>');
        }
        timecount = timecount + 1;
    }

    //Populated the table with data
    for(let ar of contaminateList) {
        data.addRows([ar]);
    }

    //identifies element table will be created at and creates the table with specific settings
    table = new google.visualization.Table(document.getElementById("output_chart"));
    table.draw(data, {showRowNumber: false, width: '100%', height: '100%', sort: 'disable', page: 'enable', pageSize: 18, allowHtml: true});

    //Applies function to all of catchment hyperlinks in the table
    for(let ar of totGraphData){
        let newLink = document.getElementById(ar[0]);
        
        //Connects links to draw a table for the individual catchment when clicked
        newLink.onclick = function() {
            catchmentArray = ar;
            drawCatchment();
            return false;
        }
    }
}

//Creates callback for catchment tables
google.charts.setOnLoadCallback(drawCatchment);

//Draws a table for individual catchments
function drawCatchment(){
    //Sets title of chart
    const outtitle = document.getElementById("output_dattitle"); 
    outtitle.innerHTML= ("Time of Travel Data for Catchment: " + catchmentArray[0]);
    
    //Defines chart and creats chart columns
    data = new google.visualization.DataTable();
    data.addColumn('string', 'Date & Time');
    data.addColumn('number', 'Velocity(m/s)');
    data.addColumn('number', 'Flow (m^3/s)');
    data.addColumn('string', 'Contaminated');
    
    //Populates the table with data
    for(let ar of catchmentArray) {
        if(ar != catchmentArray[0]){
            data.addRows([ar]);
        }
    }
    
    //Identifies element where table will be created and creates the table with specific settings
    table = new google.visualization.Table(document.getElementById("output_chart"));
    table.draw(data, {showRowNumber: false, width: '100%', height: '100%', sort: 'disable', page: 'enable', pageSize: 18, allowHtml: true});

    //Creates a hyperlink to go back to the true/false table that contains links to all catchments
    var backLink = document.createElement("a");
    var backText = document.createTextNode("Back");
    backLink.appendChild(backText);
    backLink.setAttribute('id', 'Back');
    backLink.setAttribute('href', 'Back');

    let element = document.getElementById("output_chart");
    element.appendChild(backLink);

    //Adds function to link to redraw the original table
    backLink.onclick = function(){
        drawTable();

        return false;
    }
}

function dataToCSV(){
    return google.visualization.dataTableToCsv(data);
}

function setOutputUI(){ //Called by pageSpecificLoad and multiple functions in general_page.js
    tableData = getComponentData();
    setMetadata();
    setTotOutputTable();     
    setToTOutputMap();
    setTimeout(passContam, 500);
}

function setTotOutputTable(){
    //pulls JSON from specific location
    //$.getJSON('../../../static/json/time_of_travel_nwm.json', (tableData) => {
        var dataTitle = tableData.dataset;
        var sourceTitle = tableData.dataSource;
        
        //Makes an array dateList to contain all date objects within the JSON. 
        //Also pushes to smallDateList to contain each date only once
        let dateList = [];
        for(let catchment of Object.keys(tableData.data)) {
            let dates = Object.keys(tableData.data[catchment]);
            for(let date of dates) {
            let dt = date.split(' ');
                let d = dt[0].split('-');
                if (dt.length === 2) {
                    let hr = dt[1].split(':');
                    if (hr.length === 2) {
                        dateObject = new Date(d[0], d[1] - 1, d[2], hr[0], hr[1], 0, 0);
                    }
                    else {
                        dateObject = new Date(d[0], d[1] - 1, d[2], dt[1], 0, 0, 0);
                    }
                }
                else {
                    dateObject = new Date(d[0], d[1] - 1, d[2], 0, 0, 0);
                }

                //Adds elements to global array smallDateList to contain each date only once
                if(smallDateList.length === 0){
                    smallDateList.push(dateObject + " ");
                }
                else{
                    let sameCheck = true;
                    for(let element of smallDateList){
                        if(element === (dateObject + " ")){
                            sameCheck = false;
                        }
                    }
                    if(sameCheck){
                        smallDateList.push(dateObject + " ");
                    }
                }

                dateList.push(dateObject);
            }
        }

        //Loop used to sort through the JSON and pull out all of the data
        let catchmentOnly = false;
        console.log("TempCatchData:", tableData.data);
        for(let catchment of Object.keys(tableData.data)) {
            catchmentArray = [];//resetting the global value
            let contaminantInfo = []; 
            let catchEntries = Object.entries(tableData.data[catchment]);
            //console.log("Test Data", catchEntries);
            
            let dateCounter = 0;
            let comIDLogged = true;
            for(let element of catchEntries) {
                let entry = element[1];

                //used to help sort through the date and time from within the data
                let dt = (dateList[dateCounter] + "").split(" ");
                let hr = dt[4].split(":");

                //Makes sure only the first element of a list is the com id
                if(comIDLogged){
                    catchmentArray.push(entry[0]);
                    contaminantInfo.push(('<a id="' + entry[0] + '" href="#">' + entry[0] + '</a>'));
                    comIDLogged = false;
                }

                //Pushes the data as a whole into a more organized array of the catchment's data
                let tempDataArray = [(dt[1] + " " + dt[2] + ", " + dt[3] + "  " + hr[0] + ":00"),
                    parseFloat(entry[2]),parseFloat(entry[3]),entry[4]];
                
                catchmentArray.push(tempDataArray);

                //Pushes data to a list of when the catchment first became true
                if(entry[4] === 'True') {
                    let tempDate = [entry[0], (dt[1] + " " + dt[2] + ", " + dt[3] + "  " + hr[0] + ":00"),
                    dateList[dateCounter]];

                    timeWhenTrue.push(tempDate);
                }

                //adds true and false arrays with or without color
                let doColor = true;
                if(doColor){
                    if(entry[4] === 'True'){
                        contaminantInfo.push({v: 'T', f: null, p: {style: 'background-color: lightpink;'}});
                    }
                    else{
                        contaminantInfo.push({v: 'F', f: null, p: {style: 'background-color: lightgreen;'}});
                    }
                }
                else{
                    if(entry[4] === 'True'){
                        contaminantInfo.push('T');
                    }
                    else{
                        contaminantInfo.push('F');
                    }
                }
                dateCounter = dateCounter + 1;
            }
            
            //pushes collected catchment information into arrays
            contaminateList.push(contaminantInfo);
            totGraphData.push(catchmentArray);
        }

        //this block of code is used to sort data to be in the same order as the catchments listed in the metadata
        let catchments = (tableData.metadata.catchments).split(",");
        let tempContList = [];
        let tempDataList = [];
        for(let element of catchments){
            for(let dataElement of totGraphData) {//sorts totGraphData
                if(element === dataElement[0]){
                    tempDataList.push(dataElement);
                }
            }
            for(let contElement of contaminateList){//sorts contaminateList
                let contId = contElement[0].split('"');
                if(element === contId[1]){
                    tempContList.push(contElement);
                }
            }
        }

        //sets the arrays to sorted values
        contaminateList = tempContList;
        totGraphData = tempDataList;

        console.log("Contaminated List: ", contaminateList);
        console.log("When Turned True: ", timeWhenTrue);
        console.log("Data: ", totGraphData);

        //creates new html elements to put the chart and titles within output_data rather than changing output_data as a whole
        const outdata = document.getElementById("output_data");

        var outtitle = document.createElement("h3");
        outtitle.setAttribute('id', 'output_dattitle');
        outtitle.setAttribute('class', "output_title");
        
        var outchart = document.createElement("div");
        outchart.setAttribute('id', 'output_chart');

        outdata.appendChild(outtitle);
        outdata.appendChild(outchart);

        drawTable();//calls draw table to create a chart of the data
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

        outMapData.setAttribute('id', 'output_map_data');

        outMap.setAttribute('id', 'output_map');

        outMapTitle.setAttribute('id', 'output_map_title');
        outMapTitle.setAttribute('class', 'output_title');

        let titleText = document.createTextNode("Time of Travel Map");
        outMapTitle.appendChild(titleText);

        //Used to grab the coordinate data of the catchments and put it into one list
        //https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/Catchments_NP21_Simplified/MapServer/0/query?where=FEATUREID%3D
        //&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=geojson
        //Test Com ID: 6275977
        let catchment_url_base = "https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/Catchments_NP21_Simplified/MapServer/0/query?where=FEATUREID%3D";
        let flowline_url_base = "https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/NHDSnapshot_NP21/MapServer/0/query?where=COMID%3D";

        let catchment_url_extension = "&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=geojson";
        let flowline_url_extension = "&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=geojson";

        let catchments = tableData.metadata.catchments.split(',');
        let geoCoordsList = [];  

        //For each com id, arranges query urls and queries them for the geoJSON data as well as geometries
        for(let comid of catchments){
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

                    if(Object.entries(data)[1][1][0].geometry.type === "MultiPolygon"){
                        let firstEntries = Object.entries(data)[1][1][0].geometry.coordinates[0][0][0];
                        coords = firstEntries;
                    }
                    else{
                        let firstEntries = Object.entries(data)[1][1][0].geometry.coordinates[0][0];
                        coords = firstEntries;
                    }

                    geoJSONCatchList.push([comid, data]);
                }
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
                }
            });
        }
        console.log("Geo JSON Catchments: ", geoJSONCatchList);
        console.log("Geo JSON Flowlines: ", geoJSONFlowList);
        console.log("Geo Coords list: ", geoCoordsList);

        //Take the average of the coordinate data and use it to center the map around the catchments
        let avgLAT = 0;
        let avgLNG = 0;
        for(let entry of geoCoordsList){
            avgLAT = avgLAT + entry[1][1];
            avgLNG = avgLNG + entry[1][0];

            if(entry === geoCoordsList[geoCoordsList.length - 1]){
                avgLAT = avgLAT / geoCoordsList.length;
                avgLNG = avgLNG / geoCoordsList.length;
            }
        }

        console.log("Avergae Lat: " + avgLAT + ", Average Lon: " + avgLNG);

        //Create a slider below the map to allow for date changes
        let sliderContainer = document.createElement("div");
        sliderContainer.setAttribute('class', 'slidercontainer');
        sliderContainer.setAttribute('id', 'slidercontainer');
        outMapData.appendChild(sliderContainer);

        let dateSlider = document.createElement("input");
        dateSlider.setAttribute('type', 'range');
        dateSlider.setAttribute('min', '0');
        dateSlider.setAttribute('max', (smallDateList.length - 1) + "");
        dateSlider.setAttribute('value', '0');
        dateSlider.setAttribute('class', 'slider');
        dateSlider.setAttribute('id', 'dateSlider');
        sliderContainer.appendChild(dateSlider);

        //Create date text below the slider to identify which date the user is viewing
        let slideDateDisplay = document.createElement("h4");
        slideDateDisplay.setAttribute('id', 'sliderDate');
        outMapData.appendChild(slideDateDisplay);

        //Makes an String array of the available dates for easier use
        smallDateStrings = [];
        for(let element of smallDateList){
            let dt = (element + "").split(" ");
            let hr = dt[4].split(":");

            let dateString = null;

            dateString = (dt[1] + " " + dt[2] + ", " + dt[3] + "  " + hr[0] + ":00");
            smallDateStrings.push(dateString);
        }
        slideDateDisplay.innerHTML = smallDateStrings[0];

        createMap(avgLAT, avgLNG);

        let buttonPressed = false;

        //Makes slider display the correct date
        dateSlider.oninput = function() {
            slideDateDisplay.innerHTML = smallDateStrings[this.value];
            dateSlider.setAttribute('value', this.value + "");
            makeContaminateLayer(false);

            if(buttonPressed == true){
                buttonPressed = false;
            }
        }

        let autoCycleButton = document.createElement("button");
        autoCycleButton.setAttribute('class', 'autoCycleButton');
        autoCycleButton.setAttribute('id', 'autoCycleButton');
        autoCycleButton.innerHTML = "Press to cycle through automatically";
        outMapData.appendChild(autoCycleButton);

        autoCycleButton.onclick = function(){
            buttonPressed = !buttonPressed;
            console.log("Button Pressed!, ", buttonPressed);
            setTimeout(cycle, 500);
        }

        function cycle() {
            if(buttonPressed == true){
                let val = parseInt(dateSlider.getAttribute('value')) + 1;

                if(val >= smallDateList.length){
                    dateSlider.setAttribute('value', '0');
                    $(".dateSlider").slider("refresh");
                    slideDateDisplay.innerHTML = smallDateStrings[dateSlider.value];
                    makeContaminateLayer(false);
                }
                else{
                    dateSlider.setAttribute('value', val + "");
                    $(".dateSlider").slider("refresh");
                    slideDateDisplay.innerHTML = smallDateStrings[dateSlider.value];
                    makeContaminateLayer(false);
                }
                setTimeout(cycle, 500);
            }
        }
    //});
}


function createMap(lat, lon){
    //Create the map, Jason's code
    const DEFAULT_LAT = lat;
    const DEFAULT_LNG = lon;
    const DEFAULT_ZOOM = 13;

    // catchments
    const URL_NP21_CATCHMENTS =
        "https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/Catchments_NP21_Simplified/MapServer/0";
    // WBD - HUC_8
    const URL_NP21_HUC8 =
        "https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/WBD_NP21_Simplified/MapServer/2";
    // flowlines
    const URL_NP21_FLOWLINES =
        "https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus_NP21/NHDSnapshot_NP21/MapServer/0";

    // build base map layer
    MAP = L.map("output_map").setView(
        [DEFAULT_LAT, DEFAULT_LNG],
        DEFAULT_ZOOM
    );
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution:
            'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
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
        color: "red",
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

    /*Click Interactions
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
function makeContaminateLayer(firstTime){
    let contaminateLayerOn = true;
    /*Ensures it is not adding multiple of the same layer or overlay. 
    Also helps to check whether layer is turned off in overlay options*/
    if (firstTime != true) {
        if (MAP.hasLayer(CONTAMINANT_LAYER)) {
            MAP.removeLayer(CONTAMINANT_LAYER);
            //console.log("Layer is on!");
        }
        else {
            contaminateLayerOn = false;
            //console.log("Layer is off!");
        }
        LAYER_OPTIONS.removeLayer(CONTAMINANT_LAYER);
    }

    let dateSlider = document.getElementById('dateSlider');

    /*Checks the Com IDs and the Dates to compare the time a catchment was first contaminated to 
    the current set time on the slider*/
    CONTAMINANT_LAYER = L.layerGroup();
    for (let element of geoJSONCatchList) {
        //Creates a new feature using the JSON
        let newFeature = L.geoJSON(element[1]).addTo(CONTAMINANT_LAYER);

        //Loops through times when catchments were first contaminated
        //for (let catchment of timeWhenTrue) {
            //Checks Com ID to ensure the correct geometry is changing color
           // if (catchment[0] === (element[0])) {

                newFeature.setStyle({
                    color: "black",
                    fillOpacity: 0.1,
                });
            //}
        //}
    }
    for (let element of geoJSONFlowList) {
        //Creates a new feature using the JSON
        let newFeature = L.geoJSON(element[1]).addTo(CONTAMINANT_LAYER);
        //Loops through times when catchments were first contaminated
        const contaminateCatchment = timeWhenTrue.find(catchment => {
            return catchment[0] === element[0];
        });
        //Checks Com ID to ensure the correct geometry is changing color
        if (contaminateCatchment && contaminateCatchment[1] <= smallDateStrings[dateSlider.value]) {
            //If Catchment is contaminated at current time, it will appear red
            newFeature.setStyle({
                color: "red",
            });
        }
        else {
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
    LAYER_OPTIONS.addOverlay(CONTAMINANT_LAYER, "Contaminated");
}

//Passes function without parameters used for setTimeout functions
function passContam(){
    makeContaminateLayer(true);
}