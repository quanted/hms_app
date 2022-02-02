"""
SolarCalculator Details
"""


class SolarCalculator:

    # Current module version
    version = 0.1

    # HMS module description
    description = '<p>The NOAA Solar Calculator will calculate solar data' \
                              ' for a day or a year at a specific location between the year 1901 and 2099. Equation' \
                              ' of time, Solar Declination, Apparent Sunrise and Sunset, Solar Noon, and Azimuth are ' \
                              'calculated along with several other solar data parameters. Daylight Saving Time ' \
                              'is not incorporated in this model. The table below shows respective time zones. </p>' \
                              '<img src="/hms/static/images/timezone.png " alt="Time Zone Offset" style="">'

    # Data source algorithms and brief description
    algorithms = {
        "NOAA Solar Calculator": "The equations used in the solar calculator are based on 'Astronomical Algorithms'"
                                 " by Jean Meeus. For more information about NOAA's Solar Calculator go to "
                                 "NOAA's Website.<br>Variables include:<br>Date, Time (past local midnight), "
                                 "Julian Day, Julian Century, Geom Mean Long Sun (deg), Geom Mean Anom Sun (deg), "
                                 "Eccent Earth Orbit, Sun Eq of Ctr, Sun True Long (deg), Sun True Anom (deg), "
                                 "Sun Rad Vector (AUs), Sun App Long (deg), Mean Obliq Ecliptic (deg), "
                                 "Obliq Corr (deg), Sun Rt Ascen (deg), Sun Declin (deg),var y, Eq of Time (minutes), "
                                 "HA Sunrise (deg), Solar Noon (LST), Sunrise Time (LST),Sunset Time (LST), "
                                 "Sunlight Duration (minutes), True Solar Time (min), Hour Angle (deg), "
                                 "Solar Zenith Angle (deg), Solar Elevation Angle (deg), "
                                 "Approx Atmospheric Refraction (deg), Solar Elevation corrected for "
                                 "atm refraction (deg), Solar Azimuth Angle (deg cw from N)"
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
        ["Model", "Drop-down list", "Type of model to run for the solar calculator", "Year: returns a value for each day in that year, Day: returns a value for each hour of the day."],
        ["Location Option", "Drop-down list", "Location of interest options.", "Valid options: Latitude/Longitude, Catchment Centroid. Output time-series is returned for the latitude/longitude at the centroid of the NHDPlusV2.1 catchment when 'catchment (COMID)' is selected."],
        ["Latitude", "Number", "Latitude coordinate for the output timeseries. e.g., 33.925575", "Used only when 'Latitude/Longitude' is selected for 'Location Option'."],
        ["Longitude", "Number", "Longitude coordinate for the output timeseries. e.g., -83.356893", "Used only when 'Latitude/Longitude' is selected for 'Location Option'."],
        ["Catchment COMID", "String", "NHDPlusV2.1 catchment COMID.", "Used only when 'catchment Centroid' is selected for 'Location Option'."],
        ["Timezone", "String", "Timezone of the location", "Valid timezone value [-12, +14]"],

        ["Local Time", "String", "Time for the calculation at the area of interest", "Only used with the Year model. Valid format is HH:mm:SS for hour:minutes:seconds"],
        ["Year", "String", "Year for the calculation", "Valid 4 digit year value."]
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
