"""
HMS Precipitation Compare Input form functions
"""

from django.template.loader import render_to_string
import hms_app.models.precip_compare.precip_compare_parameters as pcp


def precip_compare_input_page(request, model='', header='', form_data=None):
    """
    Constructs precipitation compare html page.
    :param request: current request object
    :param model: current model
    :param header: current header
    :param form_data: Set to None
    :return: string formatted as html
    """
    html = render_to_string('04hms_js_imports.html', {})
    html += render_to_string('04hms_input_start.html', {
        'MODEL': model,
        'TITLE': "",
    }, request=request)
    if form_data is None:
        input_form = pcp.PrecipitationCompareFormInput(request)
        html += render_to_string('04uberinput_form.html', {
            'FORM': input_form, })
    else:
        html += render_to_string('04hms_input_form.html', {
            'FORM': form_data})
    html += render_to_string('04hms_form_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    return html

