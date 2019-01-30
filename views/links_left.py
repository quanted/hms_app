"""
HMS links left function
"""

from django.template.loader import render_to_string
from collections import OrderedDict


def get_ordered_link_list(model, submodel, page=None):
    link_dict = OrderedDict([
        ('Components', OrderedDict([
            ('Watershed Workflow', 'watershed_workflow/'),
            ('Meteorology', 'meteorology/'),
            ('Hydrology', 'hydrology/'),
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
    return link_dict


def ordered_list_new(model, submodel, page=None):
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
        ('v2Hydrology', OrderedDict([
            ('Overview', 'v2hydrology/overview'),
            ('Evapotranspiration', 'v2hydrology/evapotranspiration/'),
            ('Surface Runoff', 'v2hydrology/surfacerunoff/'),
            ('Soil Moisture', 'v2hydrology/soilmoisture/'),
            ('Subsurface Flow', 'v2hydrology/subsurfaceflow/'),
        ])),
        ('Hydrodynamics', OrderedDict([
            ('Overview', 'hydrodynamic/overview'),
            ('Constant Volume', 'hydrodynamic/constant_volume'),
            ('Changing Volume', 'hydrodynamic/changing_volume'),
            ('Kinematic Wave', 'hydrodynamic/kinematic_wave'),
        ])),
        ('Components', OrderedDict([
            ('Watershed Workflow', 'watershed_workflow/'),
            ('Meteorology', 'meteorology/'),
            ('Hydrology', 'hydrology/'),
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


def ordered_list(model, submodel, page=None):
    """
    Constructs the links left menu for the hms pages.
    :param model: current model
    :param submodel: current submodel
    :param page: set to none
    :return: string containing html
    """
    # if model == "watershed":
    #     template_file = '03hms_collapsible_links_left.html'
    # elif model == "workflow" and submodel == "v2":
    #     template_file = 'workflow/hms_workflow_links_left.html'
    # elif model == "workflow":
    #     template_file = '03hms_workflow_links_left.html'
    # else:
    template_file = '03hms_links_left_drupal.html'
    link_dict = OrderedDict([
        ('Work Flows', OrderedDict([
            ('Precipitation Compare', 'workflow/precip_compare/'),
            # ('Runoff Compare', 'workflow/runoff_compare/'),
        ])),
        ('Meteorology', OrderedDict([
            ('Overview', 'meteorology/overview/'),
            ('Precipitation', 'meteorology/precipitation/'),
            ('Temperature', 'meteorology/temperature/'),
            ('Solar Calculator', 'meteorology/solarcalculator/'),
        ])),
        ('Hydrology', OrderedDict([
            ('Overview', 'hydrology/overview/'),
            ('Streamflow', 'hydrology/streamflow/'),
            ('Evapotranspiration', 'hydrology/evapotranspiration/'),
            ('Surface Runoff', 'hydrology/surfacerunoff/'),
            ('Soil Moisture', 'hydrology/soilmoisture/'),
            ('Subsurface Flow', 'hydrology/subsurfaceflow/')
        ])),
        # ('Hydrodynamics', OrderedDict([
        #     ('Overview', 'hydrodynamic/overview'),
        #     ('Constant Volume', 'hydrodynamic/constant_volume'),
        #     ('Changing Volume', 'hydrodynamic/changing_volume'),
        #     ('Kinematic Wave', 'hydrodynamic/kinematic_wave'),
        # ])),
        # ('Components', OrderedDict([
        #     ('Hydrology', 'hydrology/'),
        #     ('Water Quality', 'water_quality/')
        # ])),
        ('Utilities', OrderedDict([
            ('API Documentation', 'api_doc/'),
            ('HMS Documentation', 'docs/')
        ]))
    ])
    return render_to_string(template_file,
                            {
                                'LINK_DICT': link_dict,
                                'MODEL': model,
                                'SUBMODEL': submodel,
                                'PAGE': page
                            })
