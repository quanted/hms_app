"""
HMS links left function
"""

from django.template.loader import render_to_string
from collections import OrderedDict


def ordered_list(model, submodel, page=None):
    """
    Constructs the links left menu for the hms pages.
    :param model: current model
    :param submodel: current submodel
    :param page: set to none
    :return: string containing html
    """
    template_file = 'hms_links_left.html'
    link_dict = OrderedDict([
        ('Work Flows', OrderedDict([
            ('Overview', 'workflow/overview/'),
            ('Precipitation Data Extraction', 'workflow/precip_data_extraction/'),
            ('Precipitation Comparison', 'workflow/precip_compare/'),
            ('Streamflow', 'workflow/streamflow/'),
            ('Time of Travel', 'workflow/time_of_travel/')
        ])),
        ('Meteorology', OrderedDict([
            ('Overview', 'meteorology/overview/'),
            ('Humidity', 'meteorology/humidity/'),
            ('Precipitation', 'meteorology/precipitation/'),
            ('Radiation', 'meteorology/radiation/'),
            ('Solar Calculator', 'meteorology/solarcalculator/'),
            ('Temperature', 'meteorology/temperature/'),
            ('Wind', 'meteorology/wind/'),
        ])),
        ('Hydrology', OrderedDict([
            ('Overview', 'hydrology/overview/'),
            ('Evapotranspiration', 'hydrology/evapotranspiration/'),
            ('Surface Runoff', 'hydrology/surfacerunoff/'),
            ('Soil Moisture', 'hydrology/soilmoisture/'),
            ('Subsurface Flow', 'hydrology/subsurfaceflow/')
        ])),
        ('Documentation', OrderedDict([
            ('API Documentation', 'api_doc/'),
            ('Publications', 'docs/'),
            ('Version History', 'version_history/'),
            ('Help', 'help/')
        ]))
    ])
    return render_to_string(template_file,
                            {
                                'LINK_DICT': link_dict,
                                'MODEL': model,
                                'SUBMODEL': submodel,
                                'PAGE': page
                            })
