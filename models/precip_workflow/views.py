"""
HMS Precipitation Comparison module views
"""


header = 'HMS: Precipitation Comparison'

description = '<p>The precipitation values from the chosen NCEI Station ID and time frame are compared to the' \
              ' values from NLDAS, GLDAS, and Daymet datasets at the same location and time frame.' \
              ' A statistical analysis is performed on the values from each dataset for comparison. The average value,' \
              ' standard deviation, and total precipitation over the time period is recorded for each dataset.' \
              ' The R-squared value and a Goodness of Rainfall Estimation (GORE) index value is given to quantify' \
              ' data against NCEI precipitation data. </p>' \

algorithm = ' <br></br><p><b>Precipitation Comparison Version 1.0 Algorithms:</b>' \
			' <div align="left"> This workflow will collect precipitation data from a given NCEI Station and compare it to data obtained from NLDAS, GLDAS, and Daymet.' \
			' This comparison presents relevant metadata, a   time series graph, the Pearson''s Correlation Matrix, and a table of statistics performed on the datasets. </div></p>' \
			' <br></br><p><b>Precipitation Comparison Version 2.0 Algorithms:</b>' \
			' <div align="left"> This workflow will collect precipitation data from a given NCEI Station and compare it to data obtained from NLDAS, GLDAS, Dayment, and/or PRISM, depending on the user''s preference.' \
			' This comparison presents relevant metadata, a time series graph, the Pearson''s Correlation Matrix, and a table of statistics performed on the datasets.' \
			' <br></br><p>The user can specify an NHDPlus COM ID (catchment) or NCEI Station ID for data retrieval. If only a COM ID is provided, data from the nearest NCEI Station will be used.' \
			' If both a COM ID and NCEI Station are provided, data from the specified NCEI Station will be used.</p>' \
			' Data will be collected from January 1st of the specified start year through December 31st of the end year, and can be aggregated by Daily, Monthly, Annually, or Extreme Event temporal resolutions.' \
			' An Extreme Event is defined as an accumulation threshold of precipitation during the five preceding days or daily precipitation exceeding a specified amount.'\
			' There is no limit on the number of years that can be specified, although annual resolution requires 2 or more years, and some NCEI stations may not have data for all years.</div></p>' \
			' <br></br><p><b>Handling Missing Data:</b>' \
			' <div align="left"> Occasionally, some NCEI Stations will have periods of missing or invalid data. Days with missing data will be indicated in the output time series with values of "-9999".' \
			' However, days with missing data will be excluded for all datasets when calculating statistics. ' \
			' For extreme event aggregation, missing data will be replaced by the mean of the other datasets, or with 0 if the mean is negative.</div></p>' \
			' <br></br><p><b>Obtaining NCEI Station IDs:</b>' \
			' <div align="left"> <a href="https://www.ncdc.noaa.gov/cdo-web/datatools/findstation"> A map of NCEI Stations can be found here.</a>' \
			' The Station ID, Name, Location, and Dates can be found by clicking on the map icon.' \
			' Some stations may not show up until the map is zoomed into that location. It is recommended that you use NCEI Stations that support the "Normals Daily" Precipitation Dataset, although stations that support the "Precipitation Hourly" dataset will work as well. </div></p>' \
			' <br></br><p><b>Obtaining NHDPlus COM IDs: </b>' \
			' <div align="left"> <a href="https://epa.maps.arcgis.com/apps/webappviewer/index.html?id=ada349b90c26496ea52aab66a092593b"> A map of NHDPlus COM IDs can be found here.</a>' \
			' To find the COM ID for your region, expand the "Surface Water Features" tab, and check the box labeled "Catchments".' \
			' Click on the map to highlight a region of interest, which will bring up a window on the map. Click the three dots on the bottom right of this window and select "View in Attribute Table". This will bring up a table which contains the COM ID, which is labeled as "FeatureID".' \
			' This ID contains commas, which will need to be removed when used in Precipitation Comparison Version 2.0.</div></p>'
