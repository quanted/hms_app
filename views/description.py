"""
Generic HMS description functions
"""

from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
import importlib
import hms_app.views.links_left as links_left
import os


def get_model_header(model):
    """
    Gets the header for the given model.
    :param model: current model
    :return: string containing the model's header
    """
    model_views_location = 'hms_app.models.' + model + '.views'
    viewmodule = importlib.import_module(model_views_location)
    header = viewmodule.header
    return header


def get_model_description(model):
    """
    Gets the description for the given model.
    :param model: current model
    :return: string containing the model's description.
    """
    model_views_location = 'hms_app.models.' + model + '.views'
    viewmodule = importlib.import_module(model_views_location)
    description = viewmodule.description
    return description


def description_page(request, model, header='none'):
    """
    Base function that constructs the django HttpResponse object.
    :param request: current request
    :param model: current model
    :param header: default header
    :return: HttpResponse object of the model's description page
    """
    print("description url:" + model)
    model = model.lstrip('/')
    header = get_model_header(model)
    description = get_model_description(model)
    html = get_page_html(model, header, description)
    response = HttpResponse()
    response.write(html)
    return response


def get_page_html(model, header, description):
    """
    Constructs the html for the model's description page.
    :param model: current model
    :param header: current header
    :param description: model's description
    :return: string formatted as html for the description page
    """
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS"
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})
    if settings.IS_PUBLIC:
        pass
    else:
        html += render_to_string('06ubertext_start_index_drupal.html',{
            'TITLE': header,
            'TEXT_PARAGRAPH': description
        })
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, submodel=None)

    html += render_to_string('09epa_drupal_splashscripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html
