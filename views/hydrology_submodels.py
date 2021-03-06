"""
HMS Hydrology Submodel page functions
"""

from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
import os
import importlib
import hms_app.views.links_left as links_left
import hms_app.models.hydrology.views as hydro
import hms_app.models.hydrology.evapotranspiration_overview as evapo
import hms_app.models.hydrology.surfacerunoff_overview as runoff
import hms_app.models.hydrology.subsurfacerunoff_overview as subrunoff
import hms_app.models.hydrology.soilmoisture_overview as soilmoisture


submodel_list = ['overview', 'precipitation', 'evapotranspiration', 'soilmoisture',
                 'subsurfaceflow', 'surfacerunoff']

@ensure_csrf_cookie
def submodel_page(request, submodel, header='none'):
    """
    Base function that constructs the HttpResponse page.
    :param request: Request object
    :param submodel: 
    :param header: Default set to none
    :return: HttpResponse object.
    """
    urlpath = request.path.split('/')
    model = 'hydrology'
    submodel = urlpath[urlpath.index(model) + 1]
    header = get_submodel_header(submodel)
    html = build_submodel_page(request, model, submodel, header)
    response = HttpResponse()
    response.write(html)
    return response


def get_submodel_header(submodel):
    """
    Gets the submodel page header.
    :param submodel: Current submodel
    :return: header as a string
    """
    submodelTitle = submodel.replace('_', ' ').title()
    if (submodelTitle == "overview"):
        submodelTitle = "Overview"
    elif (submodelTitle == "Evapotranspiration"):
        submodelTitle = "Evapotranspiration"
    elif (submodelTitle == "Soilmoisture"):
        submodelTitle = "Soil Moisture"
    elif (submodelTitle == "Subsurfaceflow"):
        submodelTitle = "Subsurface Flow"
    elif (submodelTitle == "Surfacerunoff"):
        submodelTitle = "Surface Runoff"
    return hydro.header + " - " + submodelTitle


def get_submodel_description(base_url, submodel):
    """
    Gets the submodel description.
    :param submodel: Current submodel
    :return: submodel description as a string
    """
    if (submodel == "overview"):
        return hydro.description
    elif (submodel == "subsurfaceflow"):
        return build_overview_page(base_url, submodel)
    elif (submodel == "evapotranspiration"):
        return build_overview_page(base_url, submodel)
    elif (submodel == "soilmoisture"):
        return build_overview_page(base_url, submodel)
    elif (submodel == "surfacerunoff"):
        return build_overview_page(base_url, submodel)
    else:
        return hydro.unknown_description


def build_submodel_page(request, model, submodel, header):
    """
    Builds the html for the submodel page.
    :param request: default request object
    :param model: current model
    :param submodel: current submodel
    :param header: default header
    :return: returns string formatted as html
    """
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    description = get_submodel_description(submodel)
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header,
        'TEXT_PARAGRAPH': description
    })
    html += render_to_string('07ubertext_end_drupal.html', {})

    input_module = get_model_input_module(model)
    input_page_func = getattr(input_module, model + '_input_page')
    html += input_page_func(request, model, submodel, header)
    html += links_left.ordered_list(model, submodel)

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

def build_overview_page(base_url, submodel):
    details = None
    if submodel == "evapotranspiration":
        details = evapo.Evapotranspiration
    elif submodel == "surfacerunoff":
        details = runoff.SurfaceRunoff
    elif submodel == "subsurfaceflow":
        details = subrunoff.SubsurfaceRunoff
    elif submodel == "soilmoisture":
        details = soilmoisture.SoilMoisture
    html = render_to_string('hms_submodel_overview.html', {
        'MODEL': 'meteorology',
        'SUBMODEL': submodel,
        'DESCRIPTION': details.description,
        'FORMATS': details.data_format,
        'VERSION': details.version,
        'CAPABILITIES': details.capabilities,
        'SCENARIOS': details.usage,
        'SAMPLECODE': details.samples,
        'INPUTS': details.input_parameters,
        'OUTPUTS': details.output_object,
        'API': details.http_API,
        'BASEURL': base_url,
        'CHANGELOG': details.changelog
    })
    return html