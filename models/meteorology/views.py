"""
HMS Meteorology module content
"""

header = 'HMS: Meteorology'

description = 'Meteorology is the study of the atmosphere that focuses on weather processes. Precipitation, Solar data, ' \
              'and air temperature are part of the meteorology component.'

unknown_description = '<p>There is nothing for you here!</p>'

solarcalculator_description = 'Description for solar calculator. The NOAA Solar Calculator will calculate solar data' \
                              ' for a day or a year at a specific location between the year 1901 and 2099. '

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

solarcalculator_algorithm_description="The equations used in the solar calculator are based on 'Astronomical Algorithms" \
                                      "' by Jean Meeus."

temperature_algorithm_description="<p><b>NLDAS Temperature: </b>The North American Land Data Assimilation System" \
                                  " (NLDAS)" \
                                  " provides temperature measurements 2-meters above the ground in Kelvin. NLDAS" \
                                  " provides data on a 0.125-degree grid of North America. " \
                                  "<p><b>GLDAS Temperature: </b>The Global Land Data Assimilation System (GLDAS) " \
                                  "provides temperature measurements in Kelvin on" \
                                  " a .25-degree grid covering the Earth between 90 degrees North and 60 degrees South. </p>"

precipitation_algorithm_description="<p><b>NLDAS Precipitation:</b> The North American Land Data Assimilation System (NLDAS)" \
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
                            "<p><b>WGEN Precipitation:</b> WGEN is a stochastic weather generator that statistically simulates" \
                            " precipitation. WGEN uses a Markov Chain Model to determine the probability of" \
                            " precipitation occurrence. The Markov Chain Model determines precipitation by finding " \
                            " the probability of a wet day following a dry dat. Then an equation using mean daily" \
                            " rainfall, standard deviation of daily rainfall, and skew coefficients give the amount" \
                            " of rainfall on a given wet day.</p>"

