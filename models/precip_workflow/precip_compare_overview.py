"""
Precipitation Details
"""


class PrecipCompare:

    # Current module version
    version = 0.1

    # HMS module description
    description = "This workflow automatically extracts precipitation data from four national sources and compiles " \
                  "data into a consistent format. The workflow requires the user to select an NCEI station. " \
                  "Data from the user selected NCEI Station along with data from three gridded data sources " \
                  "(NLDAS, GLDAS, and TRMM) at the same location and time period are downloaded and reformatted.  " \
                  "It should be noted that dates in time-series refer to local time-zone.  The algorithm coverts " \
                  "time-series from GMT to local time-zone (of NCEI station location) for NLDAS. GLDAS, and TRMM.  " \
                  "A uniform distribution of values is assumed within a time step for gridded data sources when " \
                  "converting to local time zone. A temporal resolution of daily, or monthly can be chosen " \
                  "for data requests. Summary statistics are provided for each of the four data sources. The time " \
                  "series of data downloaded for the time period and location can be downloaded as a CSV or JSON."

    # Data source algorithms and brief description
    algorithms = {
        "Precipitation Comparison Algorithms": "This workflow will collect precipitation data from a given NCEI Station"
                                               " and compare it to data obtained from NLDAS, GLDAS, Dayment, and/or"
                                               " PRISM, depending on the user''s preference. This comparison presents"
                                               " relevant metadata, a time series graph, the Pearson''s Correlation"
                                               " Matrix, and a table of statistics performed on the datasets.'<br></br>"
                                               "<p>The user can specify an NHDPlus COMID (catchment) or NCEI Station"
                                               " ID for data retrieval. If only a COMID is provided, data from the"
                                               " nearest NCEI Station will be used. If both a COMID and NCEI Station"
                                               " are provided, data from the specified NCEI Station will be used.</p>"
                                               " Data will be collected from January 1st of the specified start year"
                                               " through December 31st of the end year, and can be aggregated by"
                                               " Daily, Monthly, Annually, or Extreme Event temporal resolutions."
                                               "An Extreme Event is defined as an accumulation threshold of "
                                               "precipitation during the five preceding days or daily precipitation "
                                               "exceeding a specified amount. There is no limit on the number of years "
                                               "that can be specified, although annual resolution requires 2 or more "
                                               "years, and some NCEI stations may not have data for all years.",
        "Handling Missing Data": "Occasionally, some NCEI Stations will have periods of missing or invalid data. Days"
                                 " with missing data will be indicated in the output time series with values of -9999."
                                 " However, days with missing data will be excluded for all datasets when calculating"
                                 " statistics. For extreme event aggregation, missing data will be replaced by the mean"
                                 " of the other datasets, or with 0 if the mean is negative.",
        "Obtaining NCEI Station IDs": "<a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation'> A map of NCEI"
                                      " Stations can be found here.</a> The Station ID, Name, Location, and Dates can "
                                      "be found by clicking on the map icon. Some stations may not show up until the "
                                      "map is zoomed into that location. It is recommended that you use NCEI Stations "
                                      "that support the 'Normals Daily' Precipitation Dataset, although stations that "
                                      "support the 'Precipitation Hourly' dataset will work as well.",
        "Obtaining NHDPlus COM IDs": " <a href='https://epa.maps.arcgis.com/apps/webappviewer/index.html?id=ada349b90c"
                                     "26496ea52aab66a092593b'> A map of NHDPlus COMIDs can be found here.</a> To "
                                     "find the COMID for your region, expand the 'Surface Water Features' tab, and "
                                     "check the box labeled 'Catchments'. Click on the map to highlight a region of "
                                     "interest, which will bring up a window on the map. Click the three dots on the "
                                     "bottom right of this window and select 'View' in Attribute Table. This will "
                                     "bring up a table which contains the COMID, which is labeled as 'FeatureID' "
                                     "This ID contains commas, which will need to be removed when used in "
                                     "Precipitation Comparison Version 2.0.",
        "NLDAS Precipitation": "The North American Land Data Assimilation System (NLDAS) combines North American radar "
                               "data and satellite data from CMORPH "
                               "(<a href='https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html' "
                               "target='_blank'>https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html</a>). "
                               "NLDAS has a one-hour time step on a 0.125-degree grid of North America, with an "
                               "average time delay of four days for data retrieval. NLDAS has data coverage from "
                               "January 1, 1979 to the present. NLDAS data are reported in UTC (GMT).",
        "GLDAS Precipitation": "The Global Land Data Assimilation System (GLDAS) combines satellite data and "
                               "ground-based observational data to provide precipitation and other meteorological "
                               "parameters. GLDAS has a three-hour time step on a global 0.25-degree grid. GLDAS-2.1 provides "
                               "data coverage from January 1, 2000 to present, with an average time delay of one month "
                               "for data retrieval. GLDAS data are reported in UTC (GMT).",
        "TRMM Precipitation": "The Tropical Rainfall Measuring Mission Multi-Satellite Precipitation Analysis Algorithm "
                              "provides precipitation estimates in specified TRMM regions from 1998 to 2019. The data is "
                              "presented in 3-hourly timesteps over a 0.25-degree spatial grid. TRMM data are reported in UTC (GMT).",
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
    # description and any child elements.
    input_parameters = [
        ["NHDPlus COMID", "String", "NHDPlusV2.1 catchment COMID.","Used only when 'catchment Centroid' is selected for 'Location Option'."],
        ["Weighted Spatial Average", "Checkbox", "Use weighted spatial average data instead of point source data.", "Spatially aggregate gridded data to NHDPlus catchment COMID."],
        ["Use NCEI Station ID", "Checkbox", "Use NCEI station as point area of interest.",
         "Allows the use of a NCEI station ID as the specified area of interest."],
        ["Data Sources", "Checkboxes", "Gridded Data Sources", "Valid sources: nldas, gldas, and trmm"],
        ["NCEI Station ID", "String", "NOAA NCEI station identification number e.g. GHCND:USW00013874",
         "Used only when “ncei” is selected for “Source”.  Station identifiers can be obtained from NOAA’s tool at <a href='https://www.ncdc.noaa.gov/cdo-web/datatools/findstation' target='_blank'>https://www.ncdc.noaa.gov/cdo-web/datatools/findstation</a>"],
        ["Start Year", "String", "Start year for the output time-series. e.g., 2010",
         "<div style='text-align:center;'>Data Availability</div><div>"
         "<br><b>nldas:</b> hourly 1/1/1979 – Present (~4-day lag); North America @ 0.125 deg resolution."
         "<br><b>gldas:</b> 3-hourly 1/1/2000-Present (~1-month lag); Global @ 0.250 deg resolution."
         "<br><b>ncei:</b> depends upon selected station"
         "<br><b>trmm:</b> daily 12/31/1997-11/30/2019; Global 50 deg South and 50 deg North latitudes @.250 deg resolution."
         "</div>", "rowspan=2"],
        ["End Year", "String", "End year for the output time-series. e.g., 2010", "", "style='display:none;'"],
        ["Temporal Aggregation", "Selection", "Temporal aggregation level of the output time-series", "Valid options: Daily, Monthly, Annual, Extreme Precipitation Event. ‘5 Day total precip threshold’ means total precipitation for the previous five days and ‘Daily precip threshold’ means precipitation for the day being compared."],
    ]

    # Output return object are provided as a list of lists, each list containing 3 elements: column,
    # datatype and description.
    output_object = [
        ["dataset", "String", "Primary dataset of the requested timeseries. Some API calls return more than one "
            " dataset,either for a workflow API or other relevent dataset."],
        ["dataSource", "String", "Primary source of the requested timeseries."],
        ["metaData", "Dictionary", "Metadata for the output timeseries, includes metadata from the source as well "
            "as HMS metadata."],
        ["data", "Dictionary", "Output timeseries data is returned as a dictionary, where the key is the datetime "
            "stamp and value is a list of values for the source/dataset."]
    ]

    # HTTP API endpoint
    http_API = [
        ["POST", "/hms/rest/api/v3/workflow/precip_compare/"]
    ]

    # Changelog is provided as a list of lists, where each list contains 3 elements: title, date, and a list of changes.
    changelog = [
        ["Version: 0.1 Beta", "May 29, 2019", ["Production UI and documentation initial setup."]]
    ]
