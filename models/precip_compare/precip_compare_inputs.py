"""
Hydrology input form
"""

from django.template.loader import render_to_string
import precip_compare_parameters

def precip_compare_input_page(request, model='', header='', form_data=None):
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

