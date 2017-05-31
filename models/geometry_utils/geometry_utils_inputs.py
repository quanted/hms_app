"""
HMS Geometry Utilities Input form function
"""

from django.template.loader import render_to_string
import os


def geometry_utils_input_page(request, model='', header='', form_data=None):
    """
    Constructs the html for the geometry input pages.
    :param request: current request object
    :param model: current model
    :param header: current header
    :param form_data: Set to None
    :return: returns a string formatted as html
    """
    backend_url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/api/WSHMS/'
    #html = render_to_string('04hms_input_jquery.html', {})
    html = render_to_string('04hms_geometry_input_start_drupal.html', {
        'MODEL': model,
        'BACKEND_URL': backend_url,
        #'TITLE': header,
    })
    if(form_data is None):
        import geometry_utils_parameters
        model_form = geometry_utils_parameters.GeometryUtilsFormInput(form_data)
        html += render_to_string('04uberinput_form.html', {
            'FORM': model_form, })
    else:
        html += render_to_string('04hms_input_form.html', {
            'FORM': form_data, })
    html += render_to_string('04hms_geometry_input_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    return html