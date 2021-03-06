"""
Evapotranspiration Details
"""


class Evapotranspiration:
    # Current module version
    version = 0.1

    # HMS module description
    description = "Evapotranspiration is the combination of water loss through a phase change by evaporation and " \
                  "transpiration. This process is the second largest component in the hydrological cycle and " \
                  "includes vaporization from water surfaces, land surfaces, and plant surfaces. Evapotranspiration " \
                  "is controlled by temperature, solar radiation, humidity, wind, and vegetation."

    # Data source algorithms and brief description
    algorithms = {
        "NLDAS Evapotranspiration": "The <a href='https://ldas.gsfc.nasa.gov/nldas' target='_blank'>North American Land "
                                    "Data Assimilation System (NLDAS)</a> combines North American radar "
                                    "data and satellite data from CMORPH "
                                    "(<a href='https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html' "
                                    "target='_blank'>https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html</a>). "
                                    "NLDAS has a one-hour time step on a 0.125-degree grid of North America, with an "
                                    "average time delay of four days for data retrieval. NLDAS has data coverage from "
                                    "January 1, 1979 to the present. NLDAS data are reported in UTC (GMT).",
        "GLDAS Evapotranspiration": "The <a href='https://ldas.gsfc.nasa.gov/gldas' target='_blank'>Global Land Data "
                                    "Assimilation System (GLDAS)</a> combines satellite data and "
                                    "ground-based observational data to provide evapotranspiration and other meteorological "
                                    "parameters. GLDAS has a three-hour time step on a global 0.25-degree grid. GLDAS-2.1 provides "
                                    "data coverage from January 1, 2000 to present, with an average time delay of one month "
                                    "for data retrieval. GLDAS data are reported in UTC (GMT).",
        "Hamon": "The Hamon algorithm calculates Potential Evapotranspiration using temperature data obtained from "
                 "NLDAS or GLDAS. The following equations are used for the calculation of Hamon PET, where H is the number of daylight hours and T<sub>mean</sub> is the average daily temperature: <img src='/static_qed/hms/images/Hamon.png' alt='Hamon equations' style=''> The following table shows all parameters used and produced by the algorithm along "
                 "with their units:<br></p><table><tr><th><b>Parameter</b></th><th><b>Units</b></th><th>Type</th></tr>"
                 "<tr><td>Min/Max/Mean Temperature</td><td>Celsius</td><td>Input</td></tr><tr><td>Sunshine Hours</td>"
                 "<td>hours</td><td>Output</td></tr><tr><td>Potential Evapotranspiration</td><td>in/day</td>"
                 "<td>Output</td></tr></table>",
        "Hargreaves": "The Hargreaves algorithm calculates Potential Evapotranspiration using temperature data obtained from "
                      "NLDAS, GLDAS, or Daymet. The following equations are used for the calculation of Hargreaves PET, where H<sub>0</sub> is the extraterrestrial radiation in MJ m<sup>-2</sup> d<sup>-1</sup> and T<sub>mn</sub>, T<sub>mx</sub>, T<sub>av</sub> are the minimum, maximum, and average daily temperatures in celsius: <img src='/static_qed/hms/images/hargreaves.PNG' alt='Hargreaves equations' style=''> The following table shows all parameters used and produced by the algorithm along "
                      "with their units:<br></p><table><tr><th><b>Parameter</b></th><th><b>Units</b></th><th>Type</th></tr>"
                      "<tr><td>Min/Max/Mean Temperature</td><td>Celsius</td><td>Input</td></tr><tr><td>Mean Solar Radiation</td>"
                      "<td>MJ m<sup>-2</sup> d<sup>-1</sup></td><td>Input</td></tr><tr><td>Potential Evapotranspiration</td><td>in/day</td>"
                      "<td>Output</td></tr></table>",
        "Penman": "The Penman algorithm calculates Potential Evapotranspiration using temperature, solar radiation, "
                  "specific humidity, and wind speed data obtained from NLDAS. Note that the Penman algorithm"
                  " also requires pressure data, which is only available from GLDAS, so GLDAS pressure data is used "
                  "regardless of the chosen data source. The images below show the main Penman ET equation as well as the equations used to calculate the individual parameters: <img src='/static_qed/hms/images/penman.png' alt='Penman equations' style=''><br><img src='/static_qed/hms/images/penmansub.PNG' alt='Penman subequations' style=''><br> where &Delta; is the slope of the saturation vapor pressure-temperature curve (kPa &deg;C<sup>-1</sup>), H<sub>net</sub> is the net radiation (MJ m<sup>-2</sup> d<sup>-1</sup>), G is the heat flux density (MJ m<sup>-2</sup> d<sup>-1</sup>), &rho;<sub>air</sub> is the air density (kg m<sup>-3</sup>), c<sub>p</sub> is the specific heat (MJ kg<sup>-1</sup> &deg;C<sup>-1</sup>), e<sup>0</sup><sub>z</sub> is the saturation vapor pressure (kPa), e<sub>z</sub> is the water vapor pressure (kPa), &gamma; is the psychrometric constant (kPa &deg;C<sup>-1</sup>), r<sub>c</sub> is the plant canopy resistance (sm<sup>-1</sup>), r<sub>a</sub> is the diffusion resistance (sm<sup>-1</sup>), and T<sub>mean</sub> is the average daily temperature (&deg;C). The following table shows all parameters used and produced by the algorithm along with their units:"
                  "</p><table><tr><th><b>Parameter</b></th><th><b>Units</b></th>"
                  "<th>Type</th></tr><tr><td>Elevation (Derived from Lat/Long)</td><td>m</td><td>Input</td></tr><tr>"
                  "<td>Albedo Coefficient</td><td>Double</td><td>Input</td></tr><tr><td>Min/Max/Mean Temperature</td>"
                  "<td>Celsius</td><td>Input</td></tr><tr><td>Mean Solar Radiation</td><td>mJ/m<sup>2</sup></td><td>Input</td>"
                  "</tr><tr><td>Mean Wind Speed</td><td>m/s</td><td>Input</td></tr><tr><td>Specific Humidity</td>"
                  "<td>kg/kg</td><td>Input</td></tr><tr><td>Mean Pressure</td><td>mbar</td><td>Input</td></tr>"
                  "<tr><td>Min/Max Relative Humidity</td><td>%</td><td>Output</td></tr>"
                  "<tr><td>Potential Evapotranspiration</td><td>in/day</td><td>Output</td></tr></table style='margin-left:auto;margin-right:auto;'>"
                  "<br><br>Further documentation of the above algorithms can be found here:<br> Neitsch, S. L., Arnold, J. G., Kiniry, J. R., & Williams, J. R. (2005, January). Soil Water and Assessment Tool Theoretical Documentation. Retrieved from https://swat.tamu.edu/media/1292/SWAT2005theory.pdf",
        "Temporal Aggregations": "The available temporal aggregations are dependent upon the native timestep size of the"
                                 " data source. Possible options include 'daily', for those sources which are not "
                                 "by default daily, and 'monthly'. Aggregated evapotranspiration data are the totals over these "
                                 "time periods and provided in the aggregated timeseries. Monthly aggregations correspond to the calendar month,"
                                 " and require the entire month to be specified in the date time span."
    }

    # Capabilities are provided as a list of capability descriptions, all html formatting must be included
    capabilities = ["Capability 1.", "Capability 2.", "Capability 3.", "Capability 4.", "Capability 5."]

    # Usage scenarios are structure as a key/value pair: the key is the title, and the value is a list containing
    # three elements: 0=Problem statement, 1=Desired Information, 2=Information Returned from Service
    usage = {"Usage Title 1": ["Problem Statement: NA 1.", "Desired Information: NA 1.",
                               "Information Returned from Service: NA 1."]}

    # Sample Code are provided as a key/value pair: key is the code language, and value is the url to the code sample github
    samples = {
        "Python": "https://github.com/quanted/hms_api_samples/blob/master/python-sample/hms-api-simple-sample.py",
        "Java": "https://github.com/quanted/hms_api_samples/blob/master/java-sample/src/com/hms/JavaSample.java",
        "C#": "https://github.com/quanted/hms_api_samples/blob/master/csharp-sample/csharp-sample/HMSSample.cs"
    }

    # Input Parameters are provided as a list of lists, each list contains 4 elements: the parameter name, type,
    # description and any child elements. Parameter names should match parameter labels in meteoroogy_parameters.py
    input_parameters = [
        ["Source", "Drop-down list", "Time-series data source",
         "Valid sources: nldas, gldas, daymet, hamon, penmandaily, hargreaves"],
        ["Start Date", "String", "Start date for the output timeseries. e.g., 01/01/2010",
         "<div style='text-align:center;'>Data Availability</div><div>"
         "<br><b>nldas:</b> hourly 1/1/1979 – Present (~4-day lag); North America @ 0.125 deg resolution."
         "<br><b>gldas:</b> 3-hourly 1/1/2000-Present (~1-month lag); Global @ 0.250 deg resolution."
         "<br><b>daymet:</b> daily 1/1/1980-Present (~1-year lag); North America @ 1-km resolution."
         "</div>", "rowspan=2"
         ],
        ["End Date", "String", "End date for the output timeseries. e.g., 01/01/2010", "", "style='display:none;'"],
        ["Weather Data Source", "Drop-down list",
         "Weather time-series data source", "Used only when selected Algorithm is not nldas or gldas. Valid options:nldas, daymet"],
        ["Location Option", "Drop-down list", "Location of interest options.",
         "Valid options: Latitude/Longitude, Catchment Centroid. Output time-series is returned for the latitude/longitude at the centroid of the NHDPlusV2.1 catchment when 'catchment (COMID)' is selected."],
        ["Latitude", "Number", "Latitude coordinate for the output timeseries. e.g., 33.925575",
         "Used only when 'Latitude/Longitude' is selected for 'Location Option'."],
        ["Longitude", "Number", "Longitude coordinate for the output timeseries. e.g., -83.356893",
         "Used only when 'Latitude/Longitude' is selected for 'Location Option'."],
        ["Catchment COMID", "String", "NHDPlusV2.1 catchment COMID.",
         "Used only when 'catchment Centroid' is selected for 'Location Option'."],
        ["Local Time", "Drop-down list", "Time zone for the timestamp in output time-series.",
         "Valid options: yes, GMT. All data sources can be returned in Greenwich Mean Time (GMT) but only nldas and gldas time-series can be returned in local time."],
        ["Temporal Resolution", "Drop-down list", "Temporal resolution/timestep of the output time-series.",
         "Valid options: hourly, 3-hourly, daily, monthly. Daily and Monthly resolution is available for all data sources.  Hourly resolution is available only for nldas.  3-hourly resolution is available for gldas."],
        ["Output Date Format", "String", "Format of the returned numeric values.",
         "Valid options: E E0, E1, E2, E3, e, e0, e1, e2, e3, F, F0, F1, F2, F3, G, G0, G1, G2, G3, N, N0, N1, N2, N3, R.  Details are available in the table below."],
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
        ["\"N\"",
         "Number.</br>Integral and decimal digits, group separators, and a decimal separator with optional negative sign.",
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
        ["dataset", "String",
         "Primary dataset of the requested timeseries. Some API calls return more than one dataset, "
         "either for a workflow API or other relevent dataset."],
        ["dataSource", "String", "Primary source of the requested timeseries."],
        ["metaData", "Dictionary", "Metadata for the output timeseries, includes metadata from the source as well "
                                   "as HMS metadata."],
        ["data", "Dictionary",
         "Output timeseries data is returned as a dictionary, where the key is the datetime stamp "
         "and value is a list of values for the source/dataset."]
    ]

    # HTTP API endpoint
    http_API = [
        ["POST", "/hms/rest/api/v3/hydrology/evapotranspiration/"]
    ]

    # Changelog is provided as a list of lists, where each list contains 3 elements: title, date, and a list of changes.
    changelog = [
        ["Version: 0.1 Beta", "May 29, 2019", ["Production UI and documentation initial setup."]]
    ]
