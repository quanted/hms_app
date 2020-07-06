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
    template_file = '03hms_links_left_drupal.html'
    link_dict = OrderedDict([
        ('Work Flows', OrderedDict([
            ('Precipitation Data Extraction', 'workflow/precip_data_extraction/'),
            ('Precipitation Comparison', 'workflow/precip_compare/'),
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
            ('Streamflow', 'hydrology/streamflow/'),
            ('Evapotranspiration', 'hydrology/evapotranspiration/'),
            ('Surface Runoff', 'hydrology/surfacerunoff/'),
            ('Soil Moisture', 'hydrology/soilmoisture/'),
            ('Subsurface Flow', 'hydrology/subsurfaceflow/')
        ])),
        ('Utilities', OrderedDict([
            ('API Documentation', 'api_doc/'),
            ('HMS Publications', 'docs/')
        ]))
    ])
    return render_to_string(template_file,
                            {
                                'LINK_DICT': link_dict,
                                'MODEL': model,
                                'SUBMODEL': submodel,
                                'PAGE': page
                            })
