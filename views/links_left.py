"""
HMS links left function
"""

from django.template.loader import render_to_string
from collections import OrderedDict
import os


def ordered_list(model, submodel, page=None):
    """
    Constructs the links left menu for the hms pages.
    :param model: current model
    :param submodel: current submodel
    :param page: set to none
    :return: string containing html
    """
    template_file = 'hms_links_left.html'
    # current_env = os.environ.get("ENV_NAME")

    if os.environ.get('HMS_AQUATOX_WEBAPP') == "True":
        link_dict = OrderedDict([
            ('Documentation', OrderedDict([
                ('Documentation', 'header'),
                ('Publications', 'docs/'),
                ('Version History', 'version_history/'),
                ('Help', 'help/'),
                ('OpenAPI', 'api_doc/')
            ])),
            ('Work Flows', OrderedDict([
                ('Work Flows', 'workflow/overview/'),
                ('Precipitation Data Extraction', 'workflow/precip_data_extraction/'),
                ('Precipitation Comparison', 'workflow/precip_compare/'),
                ('Streamflow', 'workflow/streamflow/'),
                ('Water Quality', 'webapp/')
            ])),
            ('Meteorology', OrderedDict([
                ('Meteorology', 'meteorology/overview/'),
                ('Humidity', 'meteorology/humidity/'),
                ('Precipitation', 'meteorology/precipitation/'),
                ('Radiation', 'meteorology/radiation/'),
                ('Temperature', 'meteorology/temperature/'),
                ('Wind', 'meteorology/wind/'),
            ])),
            ('Hydrology', OrderedDict([
                ('Hydrology', 'hydrology/overview/'),
                ('Evapotranspiration', 'hydrology/evapotranspiration/'),
                ('Surface Runoff', 'hydrology/surfacerunoff/'),
                ('Soil Moisture', 'hydrology/soilmoisture/'),
                ('Subsurface Flow', 'hydrology/subsurfaceflow/')
            ]))
        ])
    else:
            link_dict = OrderedDict([
            ('Documentation', OrderedDict([
                ('Documentation', 'header'),
                ('Publications', 'docs/'),
                ('Version History', 'version_history/'),
                ('Help', 'help/'),
                ('OpenAPI', 'api_doc/')
            ])),
            ('Work Flows', OrderedDict([
                ('Work Flows', 'workflow/overview/'),
                ('Precipitation Data Extraction', 'workflow/precip_data_extraction/'),
                ('Precipitation Comparison', 'workflow/precip_compare/'),
                ('Streamflow', 'workflow/streamflow/')
                #('Water Quality', 'webapp/')
            ])),
            ('Meteorology', OrderedDict([
                ('Meteorology', 'meteorology/overview/'),
                ('Humidity', 'meteorology/humidity/'),
                ('Precipitation', 'meteorology/precipitation/'),
                ('Radiation', 'meteorology/radiation/'),
                ('Temperature', 'meteorology/temperature/'),
                ('Wind', 'meteorology/wind/'),
            ])),
            ('Hydrology', OrderedDict([
                ('Hydrology', 'hydrology/overview/'),
                ('Evapotranspiration', 'hydrology/evapotranspiration/'),
                ('Surface Runoff', 'hydrology/surfacerunoff/'),
                ('Soil Moisture', 'hydrology/soilmoisture/'),
                ('Subsurface Flow', 'hydrology/subsurfaceflow/')
            ]))
        ])
    return render_to_string(template_file,

                            {
                                'LINK_DICT': link_dict,
                                'MODEL': model,
                                'SUBMODEL': submodel,
                                'PAGE': page
                            })
