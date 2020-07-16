"""
HMS Meteorology module content
"""

header = 'HMS: Meteorology'

description = 'Hydrological cycle is driven mainly by meteorological processes such as precipitation, ' \
              'evapotranspiration, energy and moisture transfer with solar radiation, temperature, and wind.  ' \
              'HMS meteorological components include precipitation, air temperature, wind, humidity, solar radiation ' \
              'and sun’s precise position calculator. The components tap into national data sources and calculators ' \
              'to retrieve and process data per user requirements. HMS meteorological components add value by ' \
              'performing operations like localizing time series data in situations where the original source of data ' \
              'report time series in Coordinated Universal Time (UTC), calculating spatially weighted average values ' \
              'time series for NHDPlus catchments from gridded datasets, locating weather station closest to a point ' \
              'location or NHDPlus catchment centroid, and temporal aggregations such as daily values from hourly data.'

unknown_description = '<p>There is nothing for you here!</p>'

solarcalculator_description = '<p>The NOAA Solar Calculator will calculate solar data' \
                              ' for a day or a year at a specific location between the year 1901 and 2099. Equation' \
                              ' of time, Solar Declination, Apparent Sunrise and Sunset, Solar Noon, and Azimuth are ' \
                              'calculated along with several other solar data parameters. Daylight Saving Time ' \
                              'is not incorporated in this model. The table below shows respective time zones. </p>' \
                              '<img src="/static_qed/hms/images/timezone.png " alt="Time Zone Offset" style="">'

radiation_description = "<p>Radiation module under development</p>"

wind_description = "<p>Wind module under development</p>"

temperature_description = "<p>Temperature module under development.</p>"

humidity_description = "<p>Humidity module is under development</p>"

solarcalculator_algorithm_description="<p>The equations used in the solar calculator are based on 'Astronomical Algorithms" \
                                      "' by Jean Meeus. For more information about NOAA's Solar Calculator go to " \
                                      "<a href='https://www.esrl.noaa.gov/gmd/grad/solcalc/calcdetails.html'> NOAA's Website.</a></p>" \
                                      "<p> Variables include:</p>" \
                                      "<p> Date, Time (past local midnight), Julian Day, Julian Century, Geom Mean Long" \
                                      " Sun (deg), Geom Mean Anom Sun (deg), Eccent Earth Orbit, Sun Eq of Ctr, Sun True" \
                                      " Long (deg), Sun True Anom (deg), Sun Rad Vector (AUs), Sun App Long (deg), " \
                                      "Mean Obliq Ecliptic (deg), Obliq Corr (deg), Sun Rt Ascen (deg), Sun Declin (deg)," \
                                      "var y, Eq of Time (minutes), HA Sunrise (deg), Solar Noon (LST), Sunrise Time (LST)," \
                                      "Sunset Time (LST), Sunlight Duration (minutes), True Solar Time (min), Hour Angle (deg)," \
                                      "	Solar Zenith Angle (deg), Solar Elevation Angle (deg), Approx Atmospheric" \
                                      " Refraction (deg), Solar Elevation corrected for atm refraction (deg), " \
                                      "Solar Azimuth Angle (deg cw from N)</p>"\

radiation_algorithm_description = "<p></p>"
wind_algorithm_description = "<p></p>"
humidity_algorithm_description = "<p></p>"

temperature_algorithm_description="<p><b>NLDAS Temperature: </b>The North American Land Data Assimilation System" \
                                  " (NLDAS)" \
                                  " provides temperature measurements 2-meters above the ground in Kelvin. NLDAS" \
                                  " provides data on a 0.125-degree grid of North America. " \
                                  "<p><b>GLDAS Temperature: </b>The Global Land Data Assimilation System (GLDAS) " \
                                  "provides temperature measurements in Kelvin on" \
                                  " a .25-degree grid covering the Earth between 90 degrees North and 60 degrees South. </p>"
