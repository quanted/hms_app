"""
TimeOfTravel Details
"""


class TimeOfTravel:

    # Current module version
    version = 0.1

    # HMS module description
    description = "This workflow calculates the time of travel for a contaminant through a network of streams based on " \
                  "the velocity and flow through the network. The workflow requires the user to select which stream " \
                  "segments the network starts and ends on. Because this workflow is a forecast tool, the time span for " \
                  "the workflow consists of an 18 hour time span starting from the current local time. The connected " \
                  "stream network is automatically generated based on the input streams, and flow data for the network " \
                  "can either be provided by the user or retrieved from the National Water Model data source. " \
                  "The resulting time series of data can be downloaded as a CSV or JSON, either per catchment or as one " \
                  "combined time series. <br \> <br \>" \

    # Data source algorithms and brief description
    algorithms = {
        "National Water Model": "The National Water Model provides gridded forecast data at one-hour time steps covering 18 hours past the current hour covering the conterminous U.S. on a 1-km grid. National Water Model data are reported in UTC (GMT)."
    }

    # Capabilities are provided as a list of capability descriptions, all html formatting must be included
    capabilities = ["Capability 1.", "Capability 2.", "Capability 3.", "Capability 4.", "Capability 5."]

    # Usage scenarios are structure as a key/value pair: the key is the title, and the value is a list containing
    # three elements: 0=Problem statement, 1=Desired Information, 2=Information Returned from Service
    usage = {"Usage Title 1": ["Problem Statement: NA 1.", "Desired Information: NA 1.", "Information Returned from Service: NA 1."]}

    # Sample Code are provided as a key/value pair: key is the code language, and value is the url to the code sample github
    samples = {
        "Python": "https://github.com/quanted/hms_api_samples/blob/master/python-sample/hms-api-simple-sample.py",
        "Java": "https://github.com/quanted/hms_api_samples/blob/master/java-sample/src/com/hms/JavaSample.java",
        "C#": "https://github.com/quanted/hms_api_samples/blob/master/csharp-sample/csharp-sample/HMSSample.cs"
    }

    # Input Parameters are provided as a list of lists, each list contains 4 elements: the parameter name, type,
    # description and any child elements. Parameter names should match parameter labels in meteoroogy_parameters.py
    input_parameters = [
    #    ["Start Date", "String", "Start date for the output timeseries. e.g., 01/01/2010",
    #                        "<div style='text-align:center;'>Data Availability</div><div>"
    #                        "<br><b>nwm:</b> hourly forecast data (18hr timeseries generated from the present time); Conterminous U.S. @ 1-km resolution."
    #                        "</div>", "rowspan=4"
    #                       ],
    #    ["Start Hour", "Number", "Start hour for the output timeseries in 24 hour time. e.g., 00-23", "", "style='display:none;'"],
    #    ["End Date", "String", "End date for the output timeseries. e.g., 01/01/2010", "", "style='display:none;'"],
    #    ["End Hour", "Number", "End hour for the output timeseries in 24 hour time. e.g., 00-23", "", "style='display:none;'"],
        ["Start COMID", "Number", "COMID for the starting NHD stream catchment.",
                            "Output time-series is returned for each catchment in the connected network between the two selected NHDPlusV2.1 catchments."
                            "</div>", "rowspan=2"
                           ],
        ["End COMID", "Number", "COMID for the ending NHD stream catchment.", "", "style='display:none;'"],
        ["Source of Streamflow Data", "Drop-down list", "Streamflow data source", "Valid sources: National Water Model, Input Table"],
        ["Contaminant Inflow", "Number", "Amount of contaminant inflow present at the given timestep in cubic meters per second.", "Used only when 'Input Table' is selected for 'Source of Streamflow Data'."]
    ]

    # Output return object are provided as a list of lists, each list containing 3 elements: column,
    # datatype and description.
    output_object = [
        ["dataset", "String", "Primary dataset of the requested timeseries. Some API calls return more than one dataset, "
                          "either for a workflow API or other relevent dataset."],
        ["dataSource", "String", "Primary source of the requested timeseries."],
        ["metaData", "Dictionary", "Metadata for the output timeseries, includes metadata from the source as well "
                               "as HMS metadata."],
        ["data", "Dictionary", "Output timeseries data is returned as a dictionary, where the key is the datetime stamp "
                           "and value is a list of values for the source/dataset."]
    ]
    
    # HTTP API endpoint
    http_API = [
        ["POST", "/hms/rest/api/v3/workflow/timeoftravel/"]
    ]

    # Changelog is provided as a list of lists, where each list contains 3 elements: title, date, and a list of changes.
    changelog = [
        ["Version: 0.1 Beta", "May 29, 2019", ["Production UI and documentation initial setup."]]
    ]
