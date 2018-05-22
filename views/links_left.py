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
    # link_dict = OrderedDict([
    #     ('Components', OrderedDict([
    #         ('Watershed Workflow', 'watershed_workflow/'),
    #         ('Meteorology', 'meteorology/'),
    #         ('hydrology', 'hydrology/'),
    #         ('Hydrodynamics', 'hydrodynamic/'),
    #         ('Water Quality', 'water_quality/')
    #     ])),
    #     ('Utilities', OrderedDict([
    #         ('API Documentation', 'api_doc/')
    #     ])),
    #     ('Work Flows', OrderedDict([
    #         ('Precipitation Compare', 'precip_compare/'),
    #         ('Runoff Compare', 'runoff_compare/'), ])),
    # ])
    print(page)

    link_dict = OrderedDict([
        ('Hydrodynamics', OrderedDict([
            ('Overview', 'hydrodynamic/overview'),
            ('Constant Volume', 'hydrodynamic/constant_volume'),
            # OrderedDict([
            #     ('Run Model', 'hydrodynamic/constant_volume/runmodel'),
            #     ('Algorithms' 'hydrodynamic/constant_volume/algorithms')]),
            ('Changing Volume', 'hydrodynamic/changing_volume'),
            ('Kinematic Wave', 'hydrodynamic/kinematic_wave'),
        ])),
        ('Components', OrderedDict([
            ('Watershed Delineation', 'watershed_workflow/'),
            ('Meteorology', 'meteorology/'),
            ('Hydrology', 'hydrology/'),
            # ('Hydrodynamics', 'hydrodynamic/'),
            ('Water Quality', 'water_quality/')
        ])),
        #('Hydrology', OrderedDict([
         #   ('Evapotranspiration', 'evap/'),
         #   ('Soil Moisture', 'soil_moist/'),
        #    ('Subsurface Flow', 'subsurface/'),
        #    ('Surface Runoff', 'runoff/'),
        #])),
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
