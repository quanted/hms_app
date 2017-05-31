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
    link_dict = OrderedDict([
        ('Components', OrderedDict([
            ('Watershed Delineation', 'watershed'),
            ('Hydrology', 'hydrology'),
            ('Water Quality', 'water_quality'),
            ('Geometry Utilities', 'geometry_utils')])),
        ('Utilities', OrderedDict([
            ('API Documentation', 'api_doc')
        ])),
        ('Work Flows', OrderedDict([
            ('Precipitation Compare', 'precip_compare'),
            ('Runoff Compare', 'runoff_compare'),])),
    ])

    return render_to_string('03ubertext_links_left_drupal_hms.html',
                            {
                                'LINK_DICT': link_dict,
                                'MODEL': model,
                                'SUBMODEL': submodel,
                                'PAGE': page
                            })
