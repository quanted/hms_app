"""
Temperature Details
"""


class Temperature:

    # Current module version
    version = 0.1

    # HMS module description
    description = "Near surface (1.5-meters to 2-meters height) air temperature plays an important role in hydrology and water quality. Evaporation from open " \
                  "water and soil surfaces is affected by air temperature. Plant transpiration and snow melts are " \
                  "also affected by air temperature. Air temperature affects water temperature and dissolved oxygen " \
                  "levels which in turn impact chemical and biological characteristics of water."

    # Data source algorithms and brief description
    algorithms = {
        "Obtaining NCEI Station IDs": "<a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation' target='_blank'> A map of NCEI"
                                      " Stations can be found here.</a> The Station ID, Name, Location, and Dates can "
                                      "be found by clicking on the map icon. Some stations may not show up until the "
                                      "map is zoomed into that location.",
        "Handling Missing Data": "Occasionally, some NCEI Stations will have periods of missing or invalid data. Days"
                                 " with missing data will be indicated in the output time series with values of -9999."
                                 " However, days with missing data will be excluded for all datasets when calculating"
                                 " statistics. ",
        "NCEI Temperature": "Stations are identified by their Station ID which includes the type of "
                            "station and the station number. Some stations have been recording data as far back as "
                            "1901 to present day. NCEI data are reported in local time zone.",
        "NLDAS Temperature": "The North American Land Data Assimilation System (NLDAS) combines North American radar "
                             "data and satellite data from CMORPH "
                             "(<a href='https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html' "
                             "target='_blank'>https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html</a>). "
                             "NLDAS has a one-hour time step on a 0.125-degree grid of North America, with an "
                             "average time delay of four days for data retrieval. NLDAS has data coverage from "
                             "January 1, 1979 to the present. NLDAS temperature data are reported in UTC (GMT) at "
                             "2-m height above surface.",
        "GLDAS Temperature": "The Global Land Data Assimilation System (GLDAS) combines satellite data and "
                             "ground-based observational data to provide temperature and other meteorological "
                             "parameters. GLDAS has a three-hour time step on a global 0.25-degree grid. GLDAS-2.1 provides "
                             "data coverage from January 1, 2000 to present, with an average time delay of one month "
                             "for data retrieval. GLDAS near surface temperature data are reported in UTC (GMT).",
        "DAYMET Temperature": "DAYMET temperature is a daily dataset of near surface air temperature that has been "
                              "interpolated and extrapolated. DAYMET uses ground station data with their model "
                              "algorithm to produce gridded estimates of daily weather parameters. The interpolated "
                              "spatial resolution is about a 0.009-degree grid over North America. Data is accessible "
                              "since 1980 to the latest full year. DAYMET discards values for December 31 from leap "
                              "years to maintain a 365-day year. DAYMET provides daily average, minimum, and maximum "
                              "temperature values.",
        "PRISM Temperature": "The Parameter-elevation Relationship on Independent Slopes Model (PRISM) is a combined "
                             "dataset consisting of ground gauge station and RADAR products. The data is on a 4km grid "
                             "resolution covering the contiguous United States. Data is available from 1981 to present. "
                             "PRISM provides daily average, minimum, and maximum air temperature data in GMT (UTC) at "
                             "2-m height above surface.",
        "Temporal Aggregations": "The available temporal aggregations are dependent upon the native timestep size of the"
                                 "data source. Possible options include 'daily', for those sources which are not "
                                 "by default daily, and 'monthly'. Aggregated temperature data is averaged over these "
                                 "time periods, as well as the minimum and maximum temperatures recorded, and provided "
                                 "in the aggregated timeseries. Monthly aggregations correspond to the calendar month,"
                                 " and require the entire month to be specified in the date time span."
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
        ["Source", "Drop-down list", "Time-series data source", "Valid sources: nldas, gldas, daymet, ncei, prism"],
        ["NCEI Station ID", "String", "NOAA NCEI station identification number e.g. GHCND:USW00013874",
         "Used only when “ncei” is selected for “Source”.  Station identifiers can be obtained from NOAA’s tool at <a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation' target='_blank'>https://www.ncdc.noaa.gov/cdo-web/datatools/findstation</a>"],
        ["Start Date", "String", "Start date for the output timeseries. e.g., 01/01/2010",
         "<div style='text-align:center;'>Data Availability</div><div>"
         "<br><b>nldas:</b> hourly 1/1/1979 – Present (~4-day lag); North America @ 0.125 deg resolution."
         "<br><b>gldas:</b> 3-hourly 1/1/2000-Present (~1-month lag); Global @ 0.250 deg resolution."
         "<br><b>daymet:</b> daily 1/1/1980-Present (~1-year lag); North America @ 1-km resolution."
         "<br><b>ncei:</b> depends upon selected station"
         "<br><b>prism:</b> daily 1/1/1981-Present (~6-month lag); Conterminous U.S. @ 4-km resolution."
         "</div>", "rowspan=2"
         ],
        ["End Date", "String", "End date for the output timeseries. e.g., 01/01/2010", "", "style='display:none;'"],
        ["Location Option", "Drop-down list", "Location of interest options.", "Valid options: Latitude/Longitude, Catchment Centroid. Output time-series is returned for the latitude/longitude at the centroid of the NHDPlusV2.1 catchment when 'catchment (COMID)' is selected."],
        ["Latitude", "Number", "Latitude coordinate for the output timeseries. e.g., 33.925575", "Used only when 'Latitude/Longitude' is selected for 'Location Option'."],
        ["Longitude", "Number", "Longitude coordinate for the output timeseries. e.g., -83.356893", "Used only when 'Latitude/Longitude' is selected for 'Location Option'."],
        ["Catchment COMID", "String", "NHDPlusV2.1 catchment COMID.", "Used only when 'catchment Centroid' is selected for 'Location Option'."],
        ["Local Time", "Drop-down list", "Time zone for the timestamp in output time-series.", "Valid options: yes, GMT. All data sources can be returned in Greenwich Mean Time (GMT) but only ncei, nldas, gldas, and trmm time-series can be returned in local time."],
        ["Temporal Resolution", "Drop-down list", "Temporal resolution/timestep of the output time-series.", "Valid options: hourly, 3-hourly, daily, monthly. Daily and Monthly resolution is available for all data sources.  Hourly resolution is available only for nldas.  3-hourly resolution is available for gldas."],
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
        ["POST", "/hms/rest/api/v3/meteorology/temperature/"]
    ]

    # Changelog is provided as a list of lists, where each list contains 3 elements: title, date, and a list of changes.
    changelog = [
        ["Version: 0.1 Beta", "May 29, 2019", ["Production UI and documentation initial setup."]]
    ]
