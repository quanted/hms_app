"""
Precipitation Details
"""


class PrecipCompare:

    # Current module version
    version = 0.1

    # HMS module description
    description = "This online tool automatically retrieves, processes, compares, and visualizes precipitation " \
                  "time-series data at point or catchment locations for selected data sources. Data covers January " \
                  "1st of the start year to December 31st of the end year and comparison statistics are provided." \
                  "</br></br>Data requests can be retrieved by (1) National Hydrography Dataset (NHDPlus V2) catchment " \
                  "identifier (COMID) or (2) NCEI gauge station identifier (Station ID). If Station ID or COMIDs are unknown," \
                  " a hyperlink is provided to a nationwide map where this information can be obtained. The" \
                  " combinations for location inputs are: (i) COMID is provided and the nearest (to catchment" \
                  " centroid) NCEI station is used, along with gridded data at catchment centroid location; (ii)" \
                  " COMID is provided, with nearest NCEI station used with spatially aggregated gridded data for" \
                  " the catchment; (iii) COMID and specific NCEI station are provided with gridded data at the" \
                  " catchment centroid; or (iv) COMID and specific NCEI station are provided with spatially" \
                  " aggregated gridded data for the catchment.</br></br> " \
                  "A temporal resolution is needed which includes daily, monthly, annual, or extreme precipitation " \
                  "event. Two user specified threshold values are required for an extreme precipitation event: one " \
                  "for rainfall accumulation for the previous five days and one for the sixth day amount. The time " \
                  "series, statistics, and metadata can be downloaded as a CSV or JSON. "

    # Data source algorithms and brief description
    algorithms = {
        "Precipitation Comparison Algorithms": "This workflow will collect precipitation data from a given NCEI Station"
                                               " and compare it to data obtained from NLDAS, GLDAS, Dayment, and/or"
                                               " PRISM, depending on the user''s preference. This comparison presents"
                                               " relevant metadata, a time series graph, the Pearson''s Correlation"
                                               " Matrix, and a table of statistics performed on the datasets.'<br></br>"
                                               "<p>The user can specify an NHDPlus COM ID (catchment) or NCEI Station"
                                               " ID for data retrieval. If only a COM ID is provided, data from the"
                                               " nearest NCEI Station will be used. If both a COM ID and NCEI Station"
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
                                      " Stations can be found here.</a> The Station ID, Name, Location, and Dates can"
                                      " be found by clicking on the map icon. Some stations may not show up until the"
                                      " map is zoomed into that location. It is recommended that you use NCEI Stations"
                                      " that support the 'Normals Daily' Precipitation Dataset, although stations that"
                                      " support the 'Precipitation Hourly' dataset will work as well.",
        "Obtaining NHDPlus COM IDs": " <a href='https://epa.maps.arcgis.com/apps/webappviewer/index.html?id=ada349b90c"
                                     "26496ea52aab66a092593b'> A map of NHDPlus COM IDs can be found here.</a> To "
                                     "find the COM ID for your region, expand the 'Surface Water Features' tab, and "
                                     "check the box labeled 'Catchments'. Click on the map to highlight a region of "
                                     "interest, which will bring up a window on the map. Click the three dots on the "
                                     "bottom right of this window and select 'View' in Attribute Table. This will "
                                     "bring up a table which contains the COM ID, which is labeled as 'FeatureI'D' "
                                     "This ID contains commas, which will need to be removed when used in "
                                     "Precipitation Comparison Version 2.0."
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
        ["Location","Parameters for NCEI Weather Observation Station","The user must select 'NHDPlus COMID' button or "
            "'NCEI Station ID' button to determine the location for precipitation comparison. See 'Data Algorithms' "
            "for more details"],
        ["NHDPlus COMID", "String", "If selected, the catchment for the user provided NHDPlus Common Identifier is"
            " used to determine which NCEI Weather Observation Station is used for comparison. e.g., 1049831"],
        ["Use weighted spatial average","Button","If selected, gridded data from selected 'Data Sources' are averaged "
             "over the 'NHDPlus COMID' catchment area for comparison."],
        ["NCEI Station ID","Button","If selected, user is presented with 'NCEI Station' String input parameter for "
             "overriding automatic selection of NCEI Station ID based on user provided 'NHDPlus COMID'."],
        ["NCEI Station","String","if 'NCEI Station ID' button is selected, this input parameter becomes visible, and "
             "the user can override automatic NCEI station selection with a user provided NCEI Station ID. e.g., "
            "'099486'"],
        ["NCEI Station ID","String","If selected, the NCEI Weather Observation Station data is compared to data in the "
            "cell from gridded 'Data Sources' containing the provided NCEI station"],
        ["Temporal","Parameters for controlling the time of the data comparison.",""],
        ["Start Year", "String", "Start Year for the output timeseries. e.g., 2010"],
        ["End Year", "String", "End Year for the output timeseries. e.g., 2012"],
        ["Temporal Aggregation","Button","the user must select the temporal resolution of the data comparison or choose"
                                         " to compare extreme precipitation events"],
        ["Data Sources","Checkbox","user must choose at least one gridded data source to compare to the NCEI Weather "
            "Observation Station associated with 'Location'"]
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
