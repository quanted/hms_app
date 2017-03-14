"""
Hydrology submodel page functions
"""

from django.template.loader import render_to_string
from django.http import HttpResponse
import os
import importlib
import links_left
import hms_app.models.hydrology.views as hydro



def submodel_page(request, submodel, header='none'):
    urlpath = request.path.split('/')
    model = urlpath[len(urlpath) - 3]
    submodel = urlpath[len(urlpath) - 2]
    header = get_submodel_header(submodel)
    html = build_submodel_page(request, model, submodel, header)
    response = HttpResponse()
    response.write(html)
    return response


def get_submodel_header(submodel):
    submodelTitle = submodel.replace('_', ' ').title()
    return hydro.header + " - " + submodelTitle


def get_submodel_description(submodel):
    if (submodel == "baseflow"):
        return hydro.baseflow_description
    elif (submodel == "evapotranspiration"):
        return hydro.evapotranspiration_description
    elif (submodel == "precipitation"):
        return hydro.precipitation_description
    elif (submodel == "soil_moisture"):
        return hydro.soil_moisture_description
    elif (submodel == "surface_runoff"):
        return hydro.surface_runoff_description
    elif (submodel == "temperature"):
        return hydro.temperature_description
    else:
        return ""


def build_submodel_page(request, model, submodel, header):
    description = get_submodel_description(submodel)
    html = render_to_string('01epa_drupal_header.html',{
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    #html += render_to_string('06ubertext_start_index_drupal.html', {
    #    'TITLE': header,
    #    'TEXT_PARAGRAPH': description
    #})

    #input form
    #condition to be removed once the other functions have been added to hydrology_parameters
    if (submodel == 'precipitation'):
        input_module = get_model_input_module(model, submodel)
        input_page_func = getattr(input_module, model + '_input_page')
        html += input_page_func(request, model, submodel, header)
    else:
        html += render_to_string('06ubertext_start_index_drupal.html', {
            'TITLE': header,
            'TEXT_PARAGRAPH': description
        })
        html += render_to_string('07ubertext_end_drupal.html', {})

    html += links_left.ordered_list(model, submodel)

    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})

    return html


def get_model_input_module(model, submodel):
    model_module_location = 'hms_app.models.' + model + '.' + model + '_inputs'
    model_input_module = importlib.import_module(model_module_location)
    return model_input_module