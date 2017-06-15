"""
HMS Geometry Utilities
"""

from django.template.loader import render_to_string
from django.http import HttpResponse
import os
import importlib
import hms_app.views.links_left as links_left


geometry_utils_description = "<p>This form provides geometry utility functions. Centroid will be calculated from the given geojson.</p>"


def form_page(request, model='Geometry Utilities', header='none'):
    """
    Form page for geometry utilities
    :param request: current request
    :param model: 'Geometry Utilities'
    :param header: default header
    :return: HttpResponse object of the geometry input form
    """
    html = build_geometry_utils_page(request, model, model)
    response = HttpResponse()
    response.write(html)
    return response


def build_geometry_utils_page(request, model, header):
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    description = geometry_utils_description
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header,
        'TEXT_PARAGRAPH': description
    })
    html += render_to_string('07ubertext_end_drupal.html', {})

    input_module = get_model_input_module("geometry_utils")
    input_page_func = getattr(input_module, 'geometry_utils_input_page')
    html += input_page_func(request, model, header)
    html += links_left.ordered_list(model, "")

    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html


def get_model_input_module(model):
    """
    Gets the object of the model containing the submodule input functions.
    :param model: current model
    :return: object of the model containing the inputs
    """
    model_module_location = 'hms_app.models.' + model + '.' + model + '_inputs'
    model_input_module = importlib.import_module(model_module_location)
    return model_input_module



