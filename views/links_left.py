from django.template.loader import render_to_string
from collections import OrderedDict

# links for 03ubertext_links_left:
def ordered_list(model, submodel, page=None):
    link_dict = OrderedDict([
        ('Components', OrderedDict([
            ('Hydrology', 'hydrology'),
            ('Water Quality', 'water_quality'),])),
        ('Utilities', OrderedDict([
            ('API Documentation', 'api_doc'),
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



