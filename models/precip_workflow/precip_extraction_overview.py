"""
Precipitation Extraction ToolDetails
"""


class PrecipExtract:

    # Current module version
    version = 0.1

    # HMS module description
    description = "This workflow automatically extracts precipitation data from 5 nationally recognized sources and compiles data into a readable format. Data from the chosen NCEI Station ID are extracted and precipitation values from all sources (NLDAS, GLDAS, Daymet, and PRISM) at the same location and time frame are also extracted. A temporal resolution of daily, weekly, or monthly can be chosen for data requests. Summary statistics are provided for each of the 5 data sources. The time series of data extracted for the time period and location can be downloaded as a CSV or JSON."

    # Data source algorithms and brief description
    algorithms = {
        "Precipitation Data Extraction Algorithms": "This workflow will collect precipitation data from a variety of data sources, including NCEI, NLDAS, GLDAS, Daymet, and PRISM. This comparison presents relevant metadata, a time series graph, the Pearsons Correlation Matrix, and a table of statistics performed on the datasets.",
        "Handling Missing Data": "Occasionally, some NCEI Stations will have periods of missing or invalid data. Days with missing data will be indicated in the output time series with values of -9999. However, days with missing data will be excluded for all datasets when calculating statistics. For extreme event aggregation, missing data will be replaced by the mean of the other datasets, or with 0 if the mean is negative.",
        "Obtaining NCEI Station IDs": "<a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation'> A map of NCEI Stations can be found here.</a> The Station ID, Name, Location, and Dates can be found by clicking on the map icon. Some stations may not show up until the map is zoomed into that location. It is recommended that you use NCEI Stations that support the 'Normals Daily' Precipitation Dataset, although stations that support the 'Precipitation Hourly' dataset will work as well."
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
    # description and any child elements.
    input_parameters = [
        ["dataset", "String", "Value: 'Precipitation'"],
        ["sourceList", "List", "Time-series precipitation data source (valid sources: nldas, gldas, daymet, ncei, prism, wgen, nwm)"],
        ["dateTimeSpan", "Dictionary", "Object holding the timeseries temporal input parameters "
                                       "(startDate, endDate, dateTimeFormat)"],
        ["startDate", "String", "Start date for the output timeseries."],
        ["endDate", "String", "End date for the output timeseries."],
        ["dateTimeFormat", "String", "Format of the datetime stamp of the output timeseries. Valid options can be found "
                                        "here: <a href=\"https://docs.microsoft.com/en-us/dotnet/api/system.datetime.tostring?view=netcore-2.2\" target=\"_blank\">Microsoft Documentation</a>"],
        ["geometry", "Dictionary", "Object holding the timeseries spatial input parameters. (point, stationID)"],
        ["point", "Dictionary", "Object holding point coordinate parameters. (latitude, longitude)"],
        ["latitude", "Number", "Latitude coordinate for the output timeseries."],
        ["longitude", "Number", "Longitude coordinate for the output timeseries."],
        ["stationID", "String", "NOAA NCEI station identification number.(Requires source to be set to 'ncei'."],
        ["dataValueFormat", "String", "Format of the output timeseries data values. Valid options can be found here: "
                                      "<a href=\"https://docs.microsoft.com/en-us/dotnet/api/system.double.tostring?view=netcore-2.2\" target=\"_blank\">Microsoft Documentation</a>"],
        ["temporalResolution", "String", "Temporal resolution/timestep of the output timeseries. Options are limited by the "
                                     "default timestep of the data source. All options are: 'default', 'daily', 'weekly', 'monthly'."],
        ["localTime", "Boolean", "Specify if the timestamp on the output timeseries is set to the timezone of the spatial area of interest."],
        ["units", "String", "Units of the output timeseries. Valid options are: 'default', 'metric', 'imperial'"],
        ["outputFormat", "String", "Format of the returned API object. Valid options are: 'json'."]
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
        ["POST", "/hms/rest/api/v3/workflow/precip_data_extraction/"]
    ]

    # Changelog is provided as a list of lists, where each list contains 3 elements: title, date, and a list of changes.
    changelog = [
        ["Version: 0.1 Beta", "May 29, 2019", ["Production UI and documentation initial setup."]]
    ]