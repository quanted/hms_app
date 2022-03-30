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
    var timeseries = dataToCSV();
    var requestJson = {
        "csrfmiddlewaretoken": getCookie("csrftoken"),
        "source": "nwm",
        "dateTimeSpan": {
            "startDate": $("#id_startDate").val() + " " + $('#id_startHour').val(),
            "endDate": $('#id_endDate').val() + " " + $('#id_endHour').val()
        },
        "geometry": {
            "geometryMetadata": {
                "startCOMID": $("#id_startCOMID").val(),
                "endCOMID": $('#id_endCOMID').val()
            }
        },
        "inflowSource": $("#id_inflowSource").val(),
        "contaminantInflow":  tableData,
        "units": "default",
        "outputFormat": "json"
    };
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

// Load the Visualization API and the piechart package.
google.charts.load('current', {'packages':['table']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawTable);

function drawTable(){
    data = new google.visualization.DataTable();
    data.addColumn('string', 'Date');
    data.addColumn('number', 'Hour');
    data.addColumn('number', 'Contaminant Inflow');
    data.addRows(tableData);

    table = new google.visualization.Table(document.getElementById('input_datatable_inner'));
    table.draw(data, {showRowNumber: false, width: '100%', height: '100%', sort: 'disable', page: 'enable', pageSize: 18});
}

function dataToCSV(){
    return google.visualization.dataTableToCsv(data);
}

function setOutputUI(){
    setMetadata();
    setTotOutputGraph();     // TO BE IMPLEMENTED
    setToTOutputMap();  // TO BE IMPLEMENTED
    return false;
}

function setTotOutputGraph(){

}

function setToTOutputMap() {

}