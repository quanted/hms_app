"""
Humidity Details
"""


class Humidity:

    # Current module version
    version = 0.1

    # HMS module description
    description = "Humidity is the measure of water vapor present in the air.  Humidity directly affects evaporation " \
                  "in hydrologic cycle.  There are several measures of humidity.  Relative humidity and dew point " \
                  "temperature are the two most commonly used measures.  Relative humidity at a given air temperature " \
                  "is the amount of water vapor in air expressed as percentage of the amount needed to achieve " \
                  "saturation at the same temperature. The dew point is the temperature the air needs to be cooled " \
                  "to in order to achieve saturation while maintaining constant pressure. If the air were to be " \
                  "cooled further, water vapor would have to come out of the atmosphere in the liquid form, usually " \
                  "as fog or precipitation."

    # Data source algorithms and brief description
    algorithms = {
        "PRISM Humidity": "The Parameter-elevation Relationship on Independent Slopes Model (PRISM) is a combined "
                          "dataset consisting of ground gauge station and RADAR products. The data is on a 4km grid "
                          "resolution covering the contiguous United States. Data is available from 1981 to present."
                          "PRISM data are reported in GMT (UTC). PRISM provides daily average temperature and "
                          "dew-point temperature data.  Relative humidity is calculated using a version of "
                          "the <a href='https://bmcnoldy.rsmas.miami.edu/Humidity.html' target='_blank'>"
                          "August-Roche-Magnus equation</a> as follows ): "
                          "RH = 100*(EXP((17.625*TD)/(243.04+TD))/EXP((17.625*T)/(243.04+T))) where, RH is % "
                          "relative humidity, TD is dew-point temperature (celsius), and T is "
                          "air temperature (celsius).",
        "Temporal Aggregations": "Possible options include 'daily' and 'monthly'. Aggregated humidity data are "
                                 "the averages over these time periods and provided in the aggregated timeseries (Rh as well as dew-point temperature)."
                                 " Monthly aggregations correspond to the calendar month, and require the entire "
                                 "month to be specified in the date time span."
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
        ["Source", "Drop-down list", "Time-series data source", "Valid sources: prism"],
        ["Parameter", "Drop-down list", "Parameter to specify the humidity dataset", "Available parameters: relative humidity, dew point"],
        ["Start Date", "String", "Start date for the output timeseries. e.g., 01/01/2010",
         "<div style='text-align:center;'>Data Availability</div><div>"
         "<br><b>prism:</b> daily 1/1/1981-Present (~6-month lag); Conterminous U.S. @ 4-km resolution."
         "</div>", "rowspan=2"
         ],
        ["End Date", "String", "End date for the output timeseries. e.g., 01/01/2010", "", "style='display:none;'"],
        ["Location Option", "Drop-down list", "Location of interest options.", "Valid options: Latitude/Longitude, Catchment Centroid. Output time-series is returned for the latitude/longitude at the centroid of the NHDPlusV2.1 catchment when 'catchment (COMID)' is selected."],
        ["Latitude", "Number", "Latitude coordinate for the output timeseries. e.g., 33.925575", "Used only when 'Latitude/Longitude' is selected for 'Location Option'."],
        ["Longitude", "Number", "Longitude coordinate for the output timeseries. e.g., -83.356893", "Used only when 'Latitude/Longitude' is selected for 'Location Option'."],
        ["Catchment COMID", "String", "NHDPlusV2.1 catchment COMID.", "Used only when 'catchment Centroid' is selected for 'Location Option'."],
        ["Local Time", "Drop-down list", "Time zone for the timestamp in output time-series.", "Valid options: GMT"],
        ["Temporal Resolution", "Drop-down list", "Temporal resolution/timestep of the output time-series.", "Valid options: daily, monthly."],
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
        ["POST", "/hms/rest/api/v3/meteorology/humidity/"]
    ]

    # Changelog is provided as a list of lists, where each list contains 3 elements: title, date, and a list of changes.
    changelog = [
        ["Version: 0.1 Beta", "May 29, 2019", ["Production UI and documentation initial setup."]]
    ]
