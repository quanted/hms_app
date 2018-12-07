"""
HMS Meteorology module content
"""

header = 'HMS: Meteorology'

description = 'HMS meteorological components include precipitation, air temperature, solar radiation and sun’s precise' \
              ' position calculator. The components tap into national data sources and calculators to retrieve and' \
              ' process data per user requirements. HMS meteorological components add value by performing operations' \
              ' like localizing time series data in situations where the original source of data report time series in' \
              ' Coordinated Universal Time (UTC), calculating spatially weighted average values time series for gridded' \
              ' datasets, and temporal aggregations such as daily values from hourly data.'

unknown_description = '<p>There is nothing for you here!</p>'

solarcalculator_description = '<p>The NOAA Solar Calculator will calculate solar data' \
                              ' for a day or a year at a specific location between the year 1901 and 2099. Equation' \
                              ' of time, Solar Declination, Apparent Sunrise and Sunset, Solar Noon, and Azimuth are ' \
                              'calculated along with several other solar data parameters. Daylight Saving Time ' \
                              'is not incorporated in this model. The table below shows respective time zones. </p>' \
                              '<img src="/static_qed/hms/images/timezone.png " alt="Time Zone Offset" style="">'

precipitation_description = "<p>Precipitation is one of the main processes in the global hydrological cycle, thus" \
                            " integral for modeling purposes. Precipitation is highly variable and influences" \
                            " vegetation, droughts, floods, and the movement of minerals and chemicals. In" \
                            " agriculture and urban areas, precipitation is the driver in contaminant and nutrient" \
                            " transport in water systems due to runoff. Precipitation data is an integral input" \
                            " for many watershed, air, erosion, and agricultural models as well as climate" \
                            " predicting projects. This data is used to determine flood/drought conditions, " \
                            "hydrologic transportation of contaminants, best management practices, and regulations." \
                            " Precipitation data is generated through direct observation as well" \
                            " as model simulation.</p>" \


temperature_description = "<p>Temperature module under development.</p>"

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

temperature_algorithm_description="<p><b>NLDAS Temperature: </b>The North American Land Data Assimilation System" \
                                  " (NLDAS)" \
                                  " provides temperature measurements 2-meters above the ground in Kelvin. NLDAS" \
                                  " provides data on a 0.125-degree grid of North America. " \
                                  "<p><b>GLDAS Temperature: </b>The Global Land Data Assimilation System (GLDAS) " \
                                  "provides temperature measurements in Kelvin on" \
                                  " a .25-degree grid covering the Earth between 90 degrees North and 60 degrees South. </p>"

precipitation_algorithm_description="<p><b>NCDC Precipitation:</b> The National Climatic Data Center (NCDC)" \
                            " provides precipitation data recorded at rain gauge stations. Stations are" \
                            "identified by their Station ID which includes the type of station and the station number. " \
                            " Some stations have been recording data as far back as 1901 to present day. " \
                            "<p><b>NLDAS Precipitation:</b> The North American Land Data Assimilation System (NLDAS)" \
                            " combines North American radar data and satellite data from CMORPH. NLDAS has an" \
                            " hourly time step on a 0.125 -degree grid of North America and has a maximum time" \
                            " lag of four days for data retrieval. Data is available from January 2, 1979 to" \
                            " present.</p>" \
                            "<p><b>GLDAS Precipitation:</b> The Global Land Data Assimilation System (GLDAS) combines" \
                            " satellite data and ground-based observational data to provide precipitation and" \
                            " other variables on a spatial resolution of 0.25-degrees covering the Earth between" \
                            " 90 degrees North and 60 degrees South. Data is available from 2000 to"\
                            " December 2016.</p>" \
                            "<p><b>DAYMET Precipitation:</b> Daymet is a daily dataset of rain gauge data that has been" \
                            " interpolated and extrapolated. Daymet uses ground station data with their model" \
                            " algorithm to produce gridded estimates of daily weather parameters. The interpolated" \
                            " spatial resolution is about a 0.009-degree grid over North America. Data is" \
                            " accessible since 1980 to the latest full year.</p>" \
                            "<p><b> PRISM Precipitation:</b> The Parameter-elevation Relationship on Independent Slopes Model" \
                            " (PRISM) is a combined dataset consisting of ground gauge station and RADAR products. The " \
                            " data is on a 4km grid resolution covering the contiguous United States. Data is available from" \
                            " 1981 to present. </p>"\
                            "<p><b>WGEN Precipitation:</b> WGEN is a stochastic weather generator that statistically simulates" \
                            " precipitation. WGEN uses a Markov Chain Model to determine the probability of" \
                            " precipitation occurrence. The Markov Chain Model determines precipitation by finding " \
                            " the probability of a wet day following a dry dat. Then an equation using mean daily" \
                            " rainfall, standard deviation of daily rainfall, and skew coefficients give the amount" \
                            " of rainfall on a given wet day.</p>"
