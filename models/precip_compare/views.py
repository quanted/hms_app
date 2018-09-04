"""
HMS Precipitation Comparison module views
"""


header = 'HMS: Precipitation Comparison'

description = '<p>The precipitation values from the chosen NCDC Station ID and time frame are compared to the' \
              ' values from NLDAS, GLDAS, and Daymet datasets at the same location and time frame.' \
              ' A statistical analysis is performed on the values from each dataset for comparison. The average value,' \
              ' standard deviation, and total precipitation over the time period is recorded for each dataset.' \
              ' The R-squared value and a Goodness of Rainfall Estimation (GORE) index value is given to quantify' \
              ' data against NCDC precipitation data. </p>' \

algorithm = ''