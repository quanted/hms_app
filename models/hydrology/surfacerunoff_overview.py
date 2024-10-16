"""
SurfaceRunoff Details
"""


class SurfaceRunoff:

    # Current module version
    version = 0.1

    # HMS module description
    description = "<p>Surface runoff is classified as precipitation that does not infiltrate into the soil" \
                  " and runs across the surface into streams, rivers, and lakes. By returning excess" \
                  " precipitation to the oceans and controlling how much water flows into the stream" \
                  " systems, runoff plays an important role in balancing the hydrological cycle. Surface" \
                  " runoff is influenced by soil properties, land cover, hillslope, and storm duration and" \
                  " intensity. Runoff is a major transporter of chemicals, pesticides, and sediments." \
                  " Runoff affects flooding, erosion, chemical concentrations, and can be classified as a" \
                  " potential source of contamination of surface waters and a nonpoint source of" \
                  " pollution.</p>"

    # Data source algorithms and brief description
    algorithms = {
        "NLDAS Surface Runoff": "The <a href='https://ldas.gsfc.nasa.gov/nldas' target='_blank'>North American Land "
                                "Data Assimilation System (NLDAS)</a> combines North American radar data and satellite data from CMORPH "
                                "(<a href='https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html' "
                                "target='_blank'>https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html</a>). "
                                "NLDAS has a one-hour time step on a 0.125-degree grid of North America, with an "
                                "average time delay of four days for data retrieval. NLDAS has data coverage from "
                                "January 1, 1979 to the present. NLDAS data are reported in UTC (GMT).",
        "GLDAS Surface Runoff": "The <a href='https://ldas.gsfc.nasa.gov/gldas' target='_blank'>Global Land Data "
                                "Assimilation System (GLDAS)</a> combines satellite data and "
                                "ground-based observational data to provide surface runoff and other hydrology "
                                "parameters. GLDAS has a three-hour time step on a global 0.25-degree grid. GLDAS-2.1 provides "
                                "data coverage from January 1, 2000 to present, with an average time delay of one month "
                                "for data retrieval. GLDAS data are reported in UTC (GMT).",
        "Curve Number": 'Curve Number algorithm in HMS is implemented using Normalized Difference Vegetation Index '
                        '(NDVI). 16-day interval NDVI satellite data from MODIS '
                        '(<a href="https://modis.gsfc.nasa.gov/data/dataprod/mod13.php" target="_blank">'
                        'https://modis.gsfc.nasa.gov/data/dataprod/mod13.php</a>) at 250 meter resolution for the '
                        'period of 2001-2018 along with soil hydrological group data was used to calculate CN for each '
                        'NHDPlus catchment. The CN calculation methodology was based on an earlier published study '
                        '(<a href="https://www.sciencedirect.com/science/article/pii/S0301479718315433" target="_blank"> '
                        'https://www.sciencedirect.com/science/article/pii/S0301479718315433</a>). More details on the '
                        'HMS CN calculation methodology are available at '
                        '(<a href="/hms/static/images/hms_cn_muche_poster_AGU_2019.pdf" target="_blank">Curve '
                        'Number Development using Normalized Difference Vegetation Index</a>).',
        "Temporal Aggregations": "The available temporal aggregations are dependent upon the native timestep size of the"
                                 " data source. Possible options include 'daily', for those sources which are not "
                                 "by default daily, and 'monthly'. Aggregated surface runoff data are the totals over these "
                                 "time periods and provided in the aggregated timeseries. Monthly aggregations correspond to the calendar month,"
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
        ["Algorithm", "Drop-down list", "Method of surface runoff calculation", "Valid sources: nldas, gldas, Curve Number"],
        ["Source", "Drop-down list", "Time-series data source", "Used only when “Curve Number” is selected for “Algorithm”. Valid sources: nldas, gldas, daymet, ncei, prism, trmm"],
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
        ["Output Data Format", "String", "Format of the returned numeric values.", "Valid options: E E0, E1, E2, E3, e, e0, e1, e2, e3, F, F0, F1, F2, F3, G, G0, G1, G2, G3, N, N0, N1, N2, N3, R.  Details are available in the table below."],
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
        ["POST", "/hms/rest/api/v3/hydrology/surfacerunoff/"]
    ]

    # Changelog is provided as a list of lists, where each list contains 3 elements: title, date, and a list of changes.
    changelog = [
        ["Version: 0.1 Beta", "May 29, 2019", ["Production UI and documentation initial setup."]]
    ]
