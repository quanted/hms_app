"""
Precipitation Details
"""


class Precipitation:

    # Current module version
    version = 0.1

    # HMS module description
    description = "Precipitation is one of the main processes in the global hydrological cycle, thus integral " \
                  "for modeling purposes. Precipitation is highly variable and influences vegetation, droughts, " \
                  "floods, and the movement of minerals and chemicals. In agriculture and urban areas, precipitation " \
                  "is the driver in contaminant and nutrient transport in water systems due to runoff. Precipitation " \
                  "data is an integral input for many watershed, air, erosion, and agricultural models as well as " \
                  "climate predicting projects. This data is used to determine flood/drought conditions, hydrologic " \
                  "transportation of contaminants, best management practices, and regulations. Precipitation data is " \
                  "generated through direct observation as well as model simulation." \
                  "<br>Precipitation data request can be submitted using one of the following two methods:" \
                  "<div style='margin-left:2em; text-align:left; margin-top:-1em;'>1.	Click on the “Data Request” tab, fill input parameter " \
                  "values, and then click on the “Submit” button. A successful submit makes “Output” tab active " \
                  "and the user is provided a data request task ID. It is recommended that the user copy the task ID. " \
                  "The user has the option to wait on the “output” tab until output data is displayed on the tab. " \
                  "For longer running data requests the user has the option to copy the task ID and leave the page. " \
                  "The user can come back later, click on the “Retrieve Data” tab, enter the task ID, and retrieve " \
                  "output data</div>." \
                  "<div style='margin-left: 2em; text-align:left; margin-top:-1em;'>2. Programmatically access RESTful API. Please navigate to " \
                  "documentation on the “Web Service Details” and “Code Samples” panels on this page.</div>"

    # Data source algorithms and brief description
    algorithms = {
        "Obtaining NCEI Station IDs": "<a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation' target='_blank'> A map of NCEI"
                                      " Stations can be found here.</a> The Station ID, Name, Location, and Dates can "
                                      "be found by clicking on the map icon. Some stations may not show up until the "
                                      "map is zoomed into that location. It is recommended that you use NCEI Stations "
                                      "that support the 'Normals Daily' Precipitation Dataset, although stations that "
                                      "support the 'Precipitation Hourly' dataset will work as well.",
        "Handling Missing Data": "Occasionally, some NCEI Stations will have periods of missing or invalid data. Days"
                                 " with missing data will be indicated in the output time series with values of -9999."
                                 " However, days with missing data will be excluded for all datasets when calculating"
                                 " statistics. For extreme event aggregation, missing data will be replaced by the mean"
                                 " of the other datasets, or with 0 if the mean is negative.",
        "NCEI Precipitation": "The National Climatic Data Center (NCEI) provides precipitation data recorded at rain "
                              "gauge stations. Stations are identified by their Station ID which includes the type of "
                              "station and the station number. Some stations have been recording data as far back as "
                              "1901 to present day.",
        "NLDAS Precipitation": "The North American Land Data Assimilation System (NLDAS) combines North American radar "
                               "data and satellite data from CMORPH "
                               "(<a href='https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html' "
                               "target='_blank'>https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html</a>). "
                               "NLDAS has a one hour time step on a 0.125-degree grid of North America, with an "
                               "average time delay of four days for data retrieval. NLDAS has data coverage from "
                               "January 1, 1979 to the present.",
        "GLDAS Precipitation": "The Global Land Data Assimilation System (GLDAS) combines satellite data and "
                               "ground-based observational data to provide precipitation and other meteorological "
                               "parameters. GLDAS has a three hour time step on a global 0.25-degree grid. GLDAS "
                               "timeseries are generated from two GLDAS products, GLDAS-2.0 and GDLAS-2.1. GLDAS-2.0 "
                               "provides data coverage from January 1, 1948 to December 31, 2010. GLDAS-2.1 provides "
                               "data coverage from January 1, 2000 to present, with an average time delay of one month "
                               "for data retrieval. GLDAS requests in HMS gives preference to GLDAS-2.1, but will "
                               "merge timeseries data, from GLDAS-2.0, for dates not available in GLDAS-2.1.",
        "DAYMET Precipitation": "DAYMET is a daily dataset of rain gauge data that has been interpolated and extrapolated. "
                                "DAYMET uses ground station data with their model algorithm to produce gridded estimates "
                                "of daily weather parameters. The interpolated spatial resolution is about a 0.009-degree "
                                "grid over North America. Data is accessible since 1980 to the latest full year. DAYMET"
                                " discards values for December 31 from leap years to maintain a 365-day year.",
        "PRISM Precipitation": "The Parameter-elevation Relationship on Independent Slopes Model (PRISM) is a combined "
                               "dataset consisting of ground gauge station and RADAR products. The data is on a 4km grid "
                               "resolution covering the contiguous United States. Data is available from 1981 to present.",
        "WGEN Precipitation": "WGEN is a stochastic weather generator that statistically simulates precipitation. WGEN "
                              "uses a Markov Chain Model to determine the probability of precipitation occurrence. The "
                              "Markov Chain Model determines precipitation by finding  the probability of a wet day "
                              "following a dry dat. Then an equation using 20-year mean daily rainfall, standard deviation of "
                              "daily rainfall, and skew coefficients give the amount of rainfall on a given wet day."
        "NWM Precipitation": "The National Water Model simulates ovserved and forecast data for hydrologic modeling. "
                              "Data is available on 1km and 250m grids that provide coverage over various lookback ranges, "
                              "varying from 3 hours to 30 days depending on the dataset."
        "TRMM Precipitation": "The Tropical Rainfall Measuring Mission Multi-satellite Precipitation Analysis Algorithm "
                              "provides precipitation estimates in specified TRMM regions from 1998 to 2019. The data is "
                              "presented in 3-hourly timesteps over a 0.25 degree spatial grid."
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
        ["Source", "Drop-Down List", "Time-series data source (valid sources: nldas, gldas, daymet, ncei, prism, wgen, nwm)"],
        ["Start Date", "String", "Start date for the output timeseries. e.g., 01/01/2010"],
        ["End Date", "String", "End date for the output timeseries. e.g., 12/31/2010"],
        ["Latitude", "Number", "Latitude coordinate for the output timeseries. e.g., 33.925575"],
        ["Longitude", "Number", "Longitude coordinate for the output timeseries. e.g., -83.356893"],
        ["NCEI Station ID", "String", "NOAA NCEI station identification number (available if source set to 'ncei'). "
                                     "e.g., GHCND:USW00013874. A tool to find a NCEI station can be found here: "
                                     "<a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation' target='_blank'>"
                                     "https://www.ncdc.noaa.gov/cdo-web/datatools/findstation</a>"],
        ["Local Time", "Drop-Down List", "Specify if the date/timestamp on the output timeseries is set to the local timezone"
                                  " ('yes') of the spatial area of interest or to GMT ('no')."],
        ["Temporal Resolution", "Drop-Down List", "Temporal resolution/timestep of the output timeseries. Options are limited"
                                          " by the default timestep of the data source. All options are: 'default',"
                                          " 'daily', 'weekly', 'monthly'."],
        ["Output Date Format", "String", "Format of the datetime stamp of the output timeseries. Valid options can be"
                                         " found here: <a href=\"https://docs.microsoft.com/en-us/dotnet/api/system."
                                         "datetime.tostring?view=netcore-2.2\" target=\"_blank\">Microsoft "
                                         "Documentation</a>"],
        ["Output Data Format", "String", "Format of the returned API object. Valid options are: 'json'."]
    ]
    '''--------------------discarded documentation:---------------------
    ["dateTimeSpan", "Dictionary", "Object holding the timeseries temporal input parameters "
                                   "(startDate, endDate, dateTimeFormat)"],
    ["geometry", "Dictionary", "Object holding the timeseries spatial input parameters. (point, stationID)"],
    ["point", "Dictionary", "Object holding point coordinate parameters. (latitude, longitude)"],
    ["dataValueFormat", "String", "Format of the output timeseries data values. Valid options can be found here: "
                                  "<a href=\"https://docs.microsoft.com/en-us/dotnet/api/system.double.tostring?view=netcore-2.2\" target=\"_blank\">Microsoft Documentation</a>"],
    ["localTime", "Boolean", "Specify if the timestamp on the output timeseries is set to the timezone of the spatial area of interest."],
    ["units", "String", "Units of the output timeseries. Valid options are: 'default', 'metric', 'imperial'"],
    '''
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
        ["POST", "/hms/rest/api/v3/meteorology/precipitation/"]
    ]

    # Changelog is provided as a list of lists, where each list contains 3 elements: title, date, and a list of changes.
    changelog = [
        ["Version: 0.1 Beta", "May 29, 2019", ["Production UI and documentation initial setup."]]
    ]
