"""
Precipitation Extraction ToolDetails
"""


class PrecipExtract:

    # Current module version
    version = 0.1

    # HMS module description
    description = "This workflow automatically extracts precipitation data from four national sources and compiles " \
                  "data into a consistent format. The workflow requires the user to select an NCEI station. " \
                  "Data from the user selected NCEI Station along with data from three gridded data sources " \
                  "(NLDAS, GLDAS, and TRMM) at the same location and time frame are downloaded and " \
                  "reformatted. It should be noted that dates in time-series refer to local time-zone. " \
                  "The algorithm converts time-series from GMT to local time-zone for NLDAS, GLDAS, and TRMM. " \
                  "A uniform distribution of values is assumed within a time step for gridded data sources when converting to local time zone. " \
                  "A temporal resolution of daily, weekly, or monthly can be chosen for data requests. " \
                  "Summary statistics are provided for each of the four data sources. The time series of data " \
                  "downloaded for the time period and location can be downloaded as a CSV or JSON."

    # Data source algorithms and brief description
    algorithms = {
        "Precipitation Data Extraction Algorithms": "This workflow will collect precipitation data from a variety of data sources, including NCEI, NLDAS, GLDAS, and TRMM. This workflow presents relevant metadata, a time series graph, the Pearson Correlation Matrix, and a table of statistics calculated on the datasets.",
        "Handling Missing Data": "Occasionally, some NCEI Stations will have periods of missing or invalid data. Days with missing data will be indicated in the output time series with values of -9999. However, days with missing data will be excluded for all datasets when calculating statistics.",
        "Obtaining NCEI Station IDs": "<a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation'> A map of NCEI Stations can be found here.</a> The Station ID, Name, Location, and Dates can be found by clicking on the map icon. Some stations may not show up until the map is zoomed into that location. It is recommended that you use NCEI Stations that support the 'Normals Daily' Precipitation Dataset, although stations that support the 'Precipitation Hourly' dataset will work as well.",
        "NLDAS Precipitation": "The North American Land Data Assimilation System (NLDAS) combines North American radar "
                               "data and satellite data from CMORPH "
                               "(<a href='https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html' "
                               "target='_blank'>https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html</a>). "
                               "NLDAS has a one-hour time step on a 0.125-degree grid of North America, with an "
                               "average time delay of four days for data retrieval. NLDAS has data coverage from "
                               "January 1, 1979 to the present. NLDAS data are reported in UTC (GMT).",
        "GLDAS Precipitation": "The Global Land Data Assimilation System (GLDAS) combines satellite data and "
                               "ground-based observational data to provide precipitation and other meteorological "
                               "parameters. GLDAS has a three-hour time step on a global 0.25-degree grid. GLDAS-2.1 provides "
                               "data coverage from January 1, 2000 to present, with an average time delay of one month "
                               "for data retrieval. GLDAS data are reported in UTC (GMT).",
        "TRMM Precipitation": "The Tropical Rainfall Measuring Mission Multi-Satellite Precipitation Analysis Algorithm "
                              "provides precipitation estimates in specified TRMM regions from 1998 to 2019. The data is "
                              "presented in 3-hourly timesteps over a 0.25-degree spatial grid. TRMM data are reported in UTC (GMT).",
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
                           ["NCEI Station ID", "String", "NOAA NCEI station identification number e.g. GHCND:USW00013874",
                            "Station identifiers can be obtained from NOAA’s tool at <a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation' target='_blank'>https://www.ncdc.noaa.gov/cdo-web/datatools/findstation</a>"],
                           ["Start Date", "String", "Start date for the output timeseries. e.g., 01/01/2010",
                            "<div style='text-align:center;'>Data Availability</div><div>"
                            "<br><b>nldas:</b> hourly 1/1/1979 – Present (~4-day lag); North America @ 0.125 deg resolution."
                            "<br><b>gldas:</b> 3-hourly 1/1/2000-Present (~1-month lag); Global @ 0.250 deg resolution."
                            "<br><b>ncei:</b> depends upon selected station"
                            "<br><b>trmm:</b> daily 12/31/1997-11/30/2019; Global 50 deg South and 50 deg North latitudes @.250 deg resolution."
                            "</div>", "rowspan=2"
                           ],
                           ["End Date", "String", "End date for the output timeseries. e.g., 01/01/2010", "", "style='display:none;'"],
                           ["Temporal Resolution", "Drop-down list", "Temporal resolution/timestep of the output time-series.", "Valid options: daily, monthly."],
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
