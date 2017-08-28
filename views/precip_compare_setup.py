"""
HMS Precipitation Comparision page functions
"""

from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
import hms_app.models.precip_compare.views as precip_compare_view
import hms_app.models.runoff_compare.views as runoff_compare_view
import os
import importlib
import hms_app.views.links_left as links_left


@ensure_csrf_cookie
def input_page(request, header='none'):
    """
    Constructs complete input page for precip compare
    :param request: current request object
    :param header: current header set to none
    :return: HttpResponse object
    """
    header = precip_compare_view.header
    html = build_page(request, "precip_compare", header)
    response = HttpResponse()
    response.write(html)
    return response


def build_page(request, model, header):
    """
    Constructs html for precip compare page
    :param request: current request object
    :param model: current model
    :param header: current header
    :return: string formatted as html
    """
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03hms_drupal_section_title.html', {})
    description = get_description(model)
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header,
        'TEXT_PARAGRAPH': description
    })
    html += render_to_string('07ubertext_end_drupal.html', {})

    input_module = get_model_input_module(model)
    input_page_func = getattr(input_module, model + '_input_page')
    html += input_page_func(request, model)
    html += links_left.ordered_list(model, "")

    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html


def get_description(model):
    if model == "precip_compare":
        return precip_compare_view.description
    elif model == "runoff_compare":
        return runoff_compare_view.description
    else:
        return ""


def get_model_input_module(model):
    """
    Gets the model input module for the input form.
    :param model: current model
    :return: input form object
    """
    model_module_location = 'hms_app.models.' + model + '.' + model + '_inputs'
    model_input_module = importlib.import_module(model_module_location)
    return model_input_module

