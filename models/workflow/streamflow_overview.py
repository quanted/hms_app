"""
Streamflow Details
"""


class Streamflow:

    # Current module version
    version = 0.1

    # HMS module description
    description = "This workflow simulates the amount of water added to an ungauged stream system during precipitation events. The user " \
                  "selects a stream network either by NHDPlus HUC ID or COMID then chooses a start and end date. A runoff" \
                  "algorithm is selected from NLDAS, GLDAS or Curve Number (CN) to calculate the amount of surface and" \
                  "subsurface runoff for each stream in the network. A precipitation source needs to be chosen from" \
                  "NLDAS, GLDAS, DAYMET, or PRISM if CN is selected as the runoff algorithm. The final input" \
                  "needed is a flow routing algorithm.  The only choice available is the constant volume algorithm." \
                  "Other algorithms such as changing volume and Kinematic wave algorithms will be implemented later." \
                  "The outputs include GMT based daily time-series of precipitation, surface runoff, subsurface flow," \
                  "and streamflow for each COMID in the network." \
                  "<img id='workflow_stream_img' src='/static_qed/hms/images/stream.jpg' alt='Some random placeholder stream'>"

    # Data source algorithms and brief description
    algorithms = {
        "Using Streamflow": "Currently, this workflow has three different stream flow algorithms: NLDAS, GLDAS, and Curve Number (CN)."
                            "To calculate Streamflow for each NHDPlus catchment in the selected stream network, data from 3 separate"
                            "datasets is downloaded simultaneously when NLDAS or GLDAS algorithm. Data for precipitation, surface"
                            "runoff, and subsurface flow is downloaded from the user-specified source in the GMT time-zone localization."
                            "Only Precipitation data in GMT is downloaded when CN is selected. Data cannot be retrieved for the user's"
                            "local time-zone.",
        "Handling Missing Data": "Depending on the size of the specified timespan and area of interest, many requests to external servers"
                                 "will need to be initiated in parallel. Occasionally, these servers will become overloaded by the volume"
                                 "of these requests and return error codes. The streamflow workflow will attempt to retry failed requests"
                                 "several times in a staggered manner. However, if they continue to fail, data for that particular segment"
                                 "will be replaced with a -9999 value.",
        "Total Flow": "The algorithm for calculating streamflow involves adding up the total flow (surface and subsurface) per"
                      "area of the stream, then checking for boundary conditions and adding in existing flow from upstream. The"
                      "workflow currently supports only the constant volume stream hydrology algorithm, but changing volume and"
                      "kinematic wave algorithms are being developed.",
        "Constant Volume Routing": "<a href='https://cfpub.epa.gov/si/si_public_record_report.cfm?Lab=NERL&dirEntryId=342907' target='_blank'>"
                                   "Flow Routing Techniques for Environmental Modeling</a> is a simple method using only the continuity "
                                   "equation where flow going out of the segment is equal tothe flow going into the segment. "
                                   "Volume, velocity, and depth remain constant with changing flows in this scheme.",
        "NLDAS and GLDAS": "NLDAS uses Noah Land Surface Model L4 (<a href='https://disc.gsfc.nasa.gov/datasets/NLDAS_NOAH0125_H_V002/summary' target='_blank'>"
                           "NLDAS Noah Land Surface Model Summary</a>) to calculate hourly surface and "
                           "subsurface runoff hourly at 0.125X0.125 degree resolution for North America.  GLDAS also uses Noah Land "
                           "Surface Model L4 (<a href='https://disc.gsfc.nasa.gov/datasets/GLDAS_NOAH025_3H_V2.1/summary' target='_blank'>"
                           "GLDAS Noad Land Surface Model Summary</a>) to calculate 3-hourly surface and "
                           "subsurface runoff at 0.25X0.25 degree resolution for most of the globe. HMS streamflow workflow downloads "
                           "NLDAS and GLDAS precipitation, surface runoff, and subsurface runoff data from "
                           "<a href='https://disc.gsfc.nasa.gov/information/tools?title=Hydrology%20Data%20Rods' target='_blank'>"
                           "NASA Hydrology Data Rods</a> and performs temporal and flow aggregations and stream network flow routing.",

        "DAYMET Precipitation": "<a href='https://daymet.ornl.gov/' target='_blank'>DAYMET</a> is a daily dataset of "
                                "rain gauge data that has been interpolated and extrapolated. "
                                "DAYMET uses ground station data with their model algorithm to produce gridded estimates "
                                "of daily weather parameters. The interpolated spatial resolution is about a 0.009-degree "
                                "grid over North America. Data is accessible since 1980 to the latest full year. DAYMET"
                                " discards values for December 31 from leap years to maintain a 365-day year. DAYMET data are reported in UTC (GMT).",
        "PRISM Precipitation": "The <a href='https://prism.oregonstate.edu/' target='_blank'>Parameter-elevation "
                               "Relationship on Independent Slopes Model (PRISM)</a> is a combined dataset consisting "
                               "of ground gauge station and RADAR products. The data is on a 4km grid "
                               "resolution covering the contiguous United States. Data is available from 1981 to present."
                               "PRISM data are reported in GMT (UTC).",
        "Curve Number": "Curve Number algorithm in HMS is implemented using Normalized Difference Vegetation Index (NDVI). "
                        "16-day interval NDVI satellite data from MODIS (<a href='https://modis.gsfc.nasa.gov/data/dataprod/mod13.php' target='_blank'>"
                        "MODIS Vegetation Index Products (NDVI and EVI)</a>) at 250 meter resolution for the period of 2001-2018 "
                        "along with soil hydrological group data was used to calculate CN for each NHDPlus catchment. "
                        "The CN calculation methodology was based on an earlier published study "
                        "(<a href='https://www.sciencedirect.com/science/article/pii/S0301479718315433' target='_blank'>"
                        "Phenology-adjusted dynamic curve number</a>). More details on the HMS CN calculation methodology are available at "
                        "(<a href='/static_qed/hms/images/hms_cn_muche_poster_AGU_2019.pdf' target='_blank'>"
                        "Curve Number Development using Normalized Difference Vegetation Index</a>). "
                        "CN algorithm in the streamflow workflow uses average curve number for the catchment being modeled."
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
                           ["Source", "Drop-down list", "Time-series data source", "Valid sources: nldas, gldas, daymet, ncei, prism, trmm"],
                           ["NCEI Station ID", "String", "NOAA NCEI station identification number e.g. GHCND:USW00013874",
                            "Used only when “ncei” is selected for “Source”.  Station identifiers can be obtained from NOAA’s tool at <a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation' target='_blank'>https://www.ncdc.noaa.gov/cdo-web/datatools/findstation</a>"],
                           ["Start Date", "String", "Start date for the output timeseries. e.g., 01/01/2010",
                            "<div style='text-align:center;'>Data Availability</div><div>"
                            "<br><b>nldas:</b> hourly 1/1/1979 – Present (~4-day lag); North America @ 0.125 deg resolution."
                            "<br><b>gldas:</b> 3-hourly 1/1/2000-Present (~1-month lag); Global @ 0.250 deg resolution."
                            "<br><b>daymet:</b> daily 1/1/1980-Present (~1-year lag); North America @ 1-km resolution."
                            "<br><b>ncei:</b> depends upon selected station. By default, 'GHCND' stations are provided at daily timesteps, 'COOP' stations are povided at hourly timesteps."
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
        ["POST", "/hms/rest/api/v3/workflow/watershed/"]
    ]

    # Changelog is provided as a list of lists, where each list contains 3 elements: title, date, and a list of changes.
    changelog = [
        ["Version: 0.1 Beta", "May 29, 2019", ["Production UI and documentation initial setup."]]
    ]
