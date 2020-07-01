"""
Precipitation Details
"""


class Precipitation:

    # Current module version
    version = 0.1

    # HMS module description
    description = "Precipitation is one of the main processes in the global hydrological cycle. Precipitation is highly variable and influences vegetation, droughts, floods, and the movement of nutrients, sediment, minerals, chemicals and other contaminants. In agriculture and urban areas, precipitation is the driver in contaminant and nutrient transport in water systems due to runoff. Precipitation data is an integral input for many watershed, air, erosion, and agricultural models as well as climate predicting projects. The data can be used in applications such as determining flood/drought conditions, hydrologic transportation of contaminants, best management practices, and regulations. Precipitation data is generated through direct observation as well as modeling.  Click on the “Data Algorithms” tab to view details of precipitation data available through HMS.  Input and output parameter descriptions are available below in the “Input Paraments” and “output Parameters” panels. Precipitation data request can be submitted using one of the following two methods:" \
                  "</br></br>" \
                  "<div style='margin-left:2em; text-align:left; margin-top:-1em;'>" \
                  "1. Click on the “Data Request” tab on this page, fill input parameter values, and then click on the “Submit” button. A successful submit makes “Output” tab active and the user is provided a data request task ID. It is recommended that the user copy the task ID. The user has the option to wait until output data is displayed on the tab. For longer running data requests the user has the option to copy the task ID and leave the page. The user can come back later, click on the “Retrieve Data” tab, enter the task ID, and retrieve output data.  Outputs are cached for 24 hours." \
                  "</div>." \
                  "<div style='margin-left: 2em; text-align:left; margin-top:-1em;'>" \
                  "2. Programmatically access RESTful API. Please navigate to documentation on the “Web Service Details” and “Code Samples” panels on this page.  Swagger implementation can be accessed by clicking on the “API Documentation” node on the left pane and then navigating to the “WSPrecipitation” service." \
                  "</div>"

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
                              "1901 to present day. NCEI data are reported in local time zone.",
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
        "DAYMET Precipitation": "DAYMET is a daily dataset of rain gauge data that has been interpolated and extrapolated. "
                                "DAYMET uses ground station data with their model algorithm to produce gridded estimates "
                                "of daily weather parameters. The interpolated spatial resolution is about a 0.009-degree "
                                "grid over North America. Data is accessible since 1980 to the latest full year. DAYMET"
                                " discards values for December 31 from leap years to maintain a 365-day year. DAYMET data are reported in UTC (GMT).",
        "PRISM Precipitation": "The Parameter-elevation Relationship on Independent Slopes Model (PRISM) is a combined "
                               "dataset consisting of ground gauge station and RADAR products. The data is on a 4km grid "
                               "resolution covering the contiguous United States. Data is available from 1981 to present."
                               "PRISM data are reported in GMT (UTC).",
        # "WGEN Precipitation": "WGEN is a stochastic weather generator that statistically simulates precipitation. WGEN "
        #                       "uses a Markov Chain Model to determine the probability of precipitation occurrence. The "
        #                       "Markov Chain Model determines precipitation by finding  the probability of a wet day "
        #                       "following a dry dat. Then an equation using 20-year mean daily rainfall, standard deviation of "
        #                       "daily rainfall, and skew coefficients calculated from DAYMET precipitation time-series"
        #                       "give the amount of rainfall on a given wet day. WGEN data are reported in GMT (UTC).",
        # "NWM Precipitation": "The National Water Model simulates ovserved and forecast data for hydrologic modeling. "
        #                       "Data is available on 1km and 250m grids that provide coverage over various lookback ranges, "
        #                       "varying from 3 hours to 30 days depending on the dataset.",
        "TRMM Precipitation": "The Tropical Rainfall Measuring Mission Multi-Satellite Precipitation Analysis Algorithm "
                              "provides precipitation estimates in specified TRMM regions from 1998 to 2019. The data is "
                              "presented in 3-hourly timesteps over a 0.25-degree spatial grid. TRMM data are reported in UTC (GMT)."
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
                           ["Source", "Drop-down list", "Time-series data source", "Valid sources: nldas, gldas, daymet, ncei, prism, wgen, trmm"],
                           ["NCEI Station ID", "String", "NOAA NCEI station identification number e.g. GHCND:USW00013874",
                            "Used only when “ncei” is selected for “Source”.  Station identifiers can be obtained from NOAA’s tool at <a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation' target='_blank'>https://www.ncdc.noaa.gov/cdo-web/datatools/findstation</a>"],
                           ["Start Date", "String", "Start date for the output timeseries. e.g., 01/01/2010",
                            "<div style='text-align:center;'>Data Availability</div><div>"
                            "<br><b>nldas:</b> hourly 1/1/1979 – Present (~4-day lag); North America @ 0.125 deg resolution."
                            "<br><b>gldas:</b> 3-hourly 1/1/2000-Present (~1-month lag); Global @ 0.250 deg resolution."
                            "<br><b>daymet:</b> daily 1/1/1980-Present (~1-year lag); North America @ 1-km resolution."
                            "<br><b>ncei:</b> depends upon selected station"
                            "<br><b>prism:</b> daily 1/1/1981-Present (~6-month lag); Conterminous U.S. @ 4-km resolution."
                            "<br><b>trmm:</b> daily 12/31/1997-11/30/2019; Global 50 deg South and 50 deg North latitudes @.250 deg resolution."
                            "</div>", "rowspan=2"
                           ],
                           ["End Date", "String", "End date for the output timeseries. e.g., 01/01/2010", "", "style='display:none;'"],
                           ["Location Option", "Drop-down list", "Location of interest options.", "Valid options: Latitude/Longitude, Catchment Centroid. Output time-series is returned for the latitude/longitude at the centroid of the NHDPlusV2.1 catchment when 'catchment (COMID)' is selected."],
                           ["Latitude", "Number", "Latitude coordinate for the output timeseries. e.g., 33.925575", "Used only when 'Latitude/Longitude' is selected for 'Location Option'."],
                           ["Longitude", "Number", "Longitude coordinate for the output timeseries. e.g., -83.356893", "Used only when 'Latitude/Longitude' is selected for 'Location Option'."],
                           ["Catchment COMID", "String", "NHDPlusV2.1 catchment COMID.", "Used only when 'catchment Centroid' is selected for 'Location Option'."],
                           ["Local Time", "Drop-down list", "Time zone for the timestamp in output time-series.", "Valid options: yes, GMT. All data sources can be returned in Greenwich Mean Time (GMT) but only ncei, nldas, gldas, and trmm time-series can be returned in local time."],
                           ["Temporal Resolution", "Drop-down list", "Temporal resolution/timestep of the output time-series.", "Valid options: hourly, 3-hourly, daily, monthly. Daily and Monthly resolution is available for all data sources.  Hourly resolution is available only for nldas.  3-hourly resolution is available for gldas, and trmm."],
                           ["Output Date Format", "String", "Format of the returned numeric values.", "Valid options: E E0, E1, E2, E3, e, e0, e1, e2, e3, F, F0, F1, F2, F3, G, G0, G1, G2, G3, N, N0, N1, N2, N3, R.  Details are available in the table below."],
    ]

    data_format = [
        ["\"E\" or \"e\"", "Exponential (Scientific).</br>Exponential notation.",
         "\"E\": 1052.0329112756 -> 1.052033E+003</br>"
         "\"e\": 1052.0329112756 -> 1.052033e+003</br>"
         "\"E2\": -1052.0329112756 -> -1.05E+003</br>"
         "\"e2\": -1052.0329112756 -> -1.05e+003</br>"],
        ["\"F\"", "Fixed-point.</br>Integral and decimal digits with optional negative sign.",
         "\"F\": 1234.567 -> 1234.57</br>"
         "\"F1\": 1234 -> 1234.0</br>"
         "\"F4\": -1234.56 -> -1234.5600</br>"],
        ["\"G\"", "General.</br>The more compact of either fixed-point or scientific notation.",
         "\"G\": -123.456 -> -123.456</br>"
         "\"G4\": 123.4546 -> 123.5</br>"
         "\"G\": -1.234567890e-25 -> -1.23456789E-25</br>"],
        ["\"N\"", "Number.</br>Integral and decimal digits, group separators, and a decimal separator with optional negative sign.",
         "\"N\": 1234.567 -> 1, 234.57</br>"
         "\"N1\": 1234 -> 1, 234.0</br>"
         "\"N3\": -1234.56 -> -1, 234.560</br>"],
        ["\"R\"", "Round-trip.</br>A string that can round-trip to an identical number.",
         "\"R\": 123456789.12345678 -> 123456789.12345678</br>"
         "\"R\": -1234567890.12345678 -> -1234567890.1234567</br>"]
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
        ["POST", "/hms/rest/api/v3/meteorology/precipitation/"]
    ]

    # Changelog is provided as a list of lists, where each list contains 3 elements: title, date, and a list of changes.
    changelog = [
        ["Version: 0.1 Beta", "May 29, 2019", ["Production UI and documentation initial setup."]]
    ]
