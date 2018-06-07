"""
HMS Hydrology module content
"""

header = 'HMS: Hydrology'

description = "<p>The hydrological cycle is the largest movement of any substance on Earth's surface with most of the" \
              " movement of water occurring through precipitation and evaporation. Controlled by the sun's radiation," \
              " water is evaporated from the ocean and land surface where it moves with the winds in the atmosphere" \
              " and condenses into clouds" \
                " to fall back down to Earth's surface as precipitation flowing toward the oceans and completing the" \
              " global hydrological cycle. All components of the hydrological cycle follow a water balance equation" \
              " which provides a basic framework for this model.</p>" \
                '<img src="/static_qed/hms/images/water_cycle.gif" alt="Hydrological Water Cycle" style="">'

unknown_description = '<p>There is nothing for you here!</p>'

subsurfaceflow_description = "<p>Subsurface flow is the flow of water beneath the Earth's surface in both the" \
                             " unsaturated and saturated zones. </p>" \


evapotranspiration_description = "<p>Evapotranspiration is the combination of water loss through a phase change by" \
                                 " evaporation and transpiration. This process is the second largest component in" \
                                 " the hydrological cycle and includes vaporization from water surfaces, land" \
                                 " surfaces, and plant surfaces.  Evapotranspiration is controlled by temperature," \
                                 "  solar radiation, humidity, wind, and vegetation.</p>"


soilmoisture_description = "<p>Soil moisture is amount of water the soil retains. When the water holding capacity" \
                           " of the soil is exceeded by precipitation the excess water is defined as surface" \
                           " runoff.</p>"

surfacerunoff_description = "<p>Surface runoff is classified as precipitation that does not infiltrate into the soil" \
                            " and runs across the surface into streams, rivers, and lakes. By returning excess" \
                            " precipitation to the oceans and controlling how much water flows into the stream" \
                            " systems, runoff plays an important role in balancing the hydrological cycle. Surface" \
                            " runoff is influenced by soil properties, land cover, hillslope, and storm duration and" \
                            " intensity. Runoff is a major transporter of chemicals, pesticides, and sediments." \
                            " Runoff affects flooding, erosion, chemical concentrations, and can be classified as a" \
                            " potential source of contamination of surface waters and a nonpoint source of" \
                            " pollution.</p>" \


subsurfaceflow_algorithm_description = "<p>The subsurface flow algorithm goes here"

evapotranspiration_algorithm_description = "<p>The table below lists the supported evapotranspiration algorithms as well as " \
                                           "the data sources that contain the required parameters for each algorithm. More" \
                                           "information regarding the inputs and outputs can be found" \
                                           "<a href='https://github.com/quanted/hms/tree/dev/Evapotranspiration'> here.</a>" \
                                       '<img src="/static_qed/hms/images/evapotable.png" alt="Evapotranspiration Inputs" style="">'

soilmoisture_algorithm_description = "<p>The NLDAS soil moisture algorithm is modeled with the NOAH community land" \
                                     " surface model. "

surfacerunoff_algorithm_description = "<p><b>NLDAS/GLDAS Surface Runoff:</b> Uses a physically distributed runoff model, NOAH, to" \
                            " calculate runoff. By calculating runoff for every grid cell, the model provides detailed" \
                            " information at various points within the catchment. An infiltration-excess based" \
                            " surface runoff scheme with a gravitational drainage subsurface runoff scheme is used" \
                            " in determining runoff for NLDAS and GLDAS. </p>" \
                            "<p><b>Curve Number Surface Runoff:</b> The SCS Curve number is an empirical method for" \
                            " calculating runoff. The curve number depends on the soil hydrologic group, rainfall" \
                            " amounts, and land cover to compute a nonlinear relationship between rainfall and runoff." \
                            " This empirical method assumes the actual runoff to potential runoff is equal to the" \
                            " ratio of actual to potential retention. </p>" \
