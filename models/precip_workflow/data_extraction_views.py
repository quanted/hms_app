"""
HMS Precipitation Comparison module views
"""


header = 'HMS: Precipitation Data Extraction.'

description = '<p>Replace with details about precipitation data extraction tool.</p>' \

algorithm = ' <br></br><p><b>Precipitation Data Extraction Algorithms:</b>' \
			' <div align="left"> This workflow will collect precipitation data from a variety of data sources, including NCEI, NLDAS, GLDAS, Daymet, and PRISM.' \
			' This comparison presents relevant metadata, a   time series graph, the Pearson''s Correlation Matrix, and a table of statistics performed on the datasets. </div></p>' \
			' <br></br><p><b>Handling Missing Data:</b>' \
			' <div align="left"> Occasionally, some NCEI Stations will have periods of missing or invalid data. Days with missing data will be indicated in the output time series with values of "-9999".' \
			' However, days with missing data will be excluded for all datasets when calculating statistics. ' \
			' For extreme event aggregation, missing data will be replaced by the mean of the other datasets, or with 0 if the mean is negative.</div></p>' \
			' <br></br><p><b>Obtaining NCEI Station IDs:</b>' \
			' <div align="left"> <a href="https://www.ncdc.noaa.gov/cdo-web/datatools/findstation"> A map of NCEI Stations can be found here.</a>' \
			' The Station ID, Name, Location, and Dates can be found by clicking on the map icon.' \

