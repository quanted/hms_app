"""
HMS Precipitation Compare Input form functions
"""

from django.template.loader import render_to_string
import precip_compare_parameters


def precip_compare_input_page(request, model='', header='', form_data=None):
    """
    Constructs precipitation compare html page.
    :param request: current request object
    :param model: current model
    :param header: current header
    :param form_data: Set to None
    :return: string formatted as html
    """
    html = render_to_string('04hms_input_jquery.html', {})
    html += render_to_string('04hms_input_start_drupal.html', {
        'MODEL': model,
        'TITLE': "",
    })
    input_form = precip_compare_parameters.PrecipitationCompareFormInput(form_data)
    html += render_to_string('04uberinput_form.html', {
        'FORM': input_form, })
    html += render_to_string('04uberinput_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    return html

