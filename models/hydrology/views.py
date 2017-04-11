"""
Hydrology module content
"""

header = 'HMS: Hydrology'

description = "<p>The hydrological cycle is the largest movement of any substance on Earth with most of the movement occurring through precipitation and evaporation. Controlled by the sun's radiation, water is evaporated from the ocean and land surface where it moves with the winds in the atmosphere and condenses into clouds" \
                " to fall back down to Earth's surface as precipitation flowing toward the oceans and completing the global hydrological cycle. All components of the hydrological cycle follow a water balance equation which provides a basic framework for this model.</p>" \
                '<img src="/static_qed/hms/img/water_cycle.png" alt="Hydrological Water Cycle" style="">'

unknown_description = '<p>There is nothing for you here!</p>'

baseflow_description = "<p>Baseflow is the portion of streamflow that comes from subsurface groundwater effluent.</p>" \
                        "<p>NLDAS baseflow: is the subsurface runoff</p>"

evapotranspiration_description = "<p>Evapotranspiration is the combination of water loss through a phase change by evaporation and transpiration. This process is the second largest component in the hydrological cycle and includes vaporization from water surfaces, land surfaces, and plant surfaces.  Controlled by temperature, solar radiation, humidity, wind, and vegetation.</p>"

precipitation_description = "<p>Precipitation is one of the main processes in the global hydrological cycle thus integral for modeling purposes. Precipitation is highly variable and influences vegetation, droughts, floods, and the movement of minerals and chemicals. In agriculture and urban areas, precipitation is the driver in contaminant and nutrient transport in water systems due to runoff. Precipitation data is an integral input for many watershed, air, erosion, and agricultural models as well as climate predicting projects. This data is used to determine flood/drought conditions, hydrologic transportation of contaminants, best management practices, and regulations. Precipitation data is generated through direct observation as well as model simulation.</p>" \
                            "<p>NLDAS Precipitation: The North American Land Data Assimilation System (NLDAS) combines North American radar data and satellite data from CMORPH. NLDAS has an hourly time step on a 0.125 -degree grid of North America and has a maximum time lag of four days for data retrieval. Data is available from January 2, 1979 to present.</p>" \
                            "<p>GLDAS precipitation: The Global Land Data Assimilation System (GLDAS) combines satellite data and ground-based observational data to provide precipitation and other variables on a spatial resolution of 0.25-degrees covering the Earth between 90 degrees North and 60 degrees South. Data is available from 2000 to present.</p>" \
                            "<p>DAYMET precipitation: Daymet is a daily dataset of rain gauge data that has been interpolated and extrapolated. Daymet uses ground station data with their model algorithm to produce gridded estimates of daily weather parameters. The interpolated spatial resolution is about a 0.009-degree grid over North America. Data is accessible since 1980 to the latest full year.</p>"

soilmoisture_description = "<p>Soil moisture is amount of water the soil retains. When the water holding capacity of the soil is exceeded by precipitation the excess water is defined as surface runoff.</p>"

surfacerunoff_description = "<p>Surface runoff is classified as precipitation that does not infiltrate into the soil and runs across the surface into streams, rivers, and lakes. Depends on soil moisture, impervious areas, hillslope, and storm intensity.  Affects flooding, sediment transport, erosion, and chemical concentrations.</p>" \
                            "<p>NLDAS/GLDAS Runoff: Uses the VIC model to calculate runoff.</p>"

temperature_description = "<p>Temperature module under development.</p>"
