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
        ('Meteorology', OrderedDict([
            ('Overview', 'meteorology/overview'),
            ('Precipitation', 'meteorology/precipitation'),
            ('Temperature', 'meteorology/temperature'),
            ('Solar Calculator', 'meteorology/solarcalculator'),
        ])),
        ('Hydrology', OrderedDict([
            ('Overview', 'hydrology/overview'),
            ('Evapotranspiration', 'hydrology/evapotranspiration/'),
            ('Surface Runoff', 'hydrology/surfacerunoff/'),
            ('Soil Moisture', 'hydrology/soilmoisture/'),
            ('Subsurface Flow', 'hydrology/subsurfaceflow/'),
        ])),
        ('Hydrodynamics', OrderedDict([
            ('Overview', 'hydrodynamic/overview'),
            ('Constant Volume', 'hydrodynamic/constant_volume'),
            ('Changing Volume', 'hydrodynamic/changing_volume'),
            ('Kinematic Wave', 'hydrodynamic/kinematic_wave'),
        ])),
        ('Components', OrderedDict([
            ('Watershed Delineation', 'watershed_workflow/'),
            #('Meteorology', 'meteorology/'),
            #('Hydrology', 'hydrology/'),
            ('Water Quality', 'water_quality/')
        ])),
        ('Utilities', OrderedDict([
            ('API Documentation', 'api_doc/'),
            ('HMS Documentation', 'Documents/')
        ])),
        ('Work Flows', OrderedDict([
            ('Precipitation Compare', 'precip_compare/'),
            ('Runoff Compare', 'runoff_compare/'), ])),
    ])

    if model == "watershed":
        return render_to_string('03hms_collapsible_links_left.html',
                                {
                                    'LINK_DICT': link_dict,
                                    'MODEL': model,
                                    'SUBMODEL': submodel,
                                    'PAGE': page
                                })
    elif model == "workflow":
        return render_to_string('03hms_workflow_links_left.html',
                                {
                                    'LINK_DICT': link_dict,
                                    'MODEL': model,
                                    'SUBMODEL': submodel,
                                    'PAGE': page
                                })
    else:
        return render_to_string('03ubertext_links_left_drupal_hms.html',
                                {
                                    'LINK_DICT': link_dict,
                                    'MODEL': model,
                                    'SUBMODEL': submodel,
                                    'PAGE': page
                                })