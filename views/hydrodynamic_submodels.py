"""
HMS Hydrodynamic Submodel page functions
"""

from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
import os
import importlib
import hms_app.views.links_left as links_left
import hms_app.models.hydrodynamic.views as hydro_d


submodel_list = ['overview', 'constant_volume', 'changing_volume',
                 'kinematic_wave']

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
    model = 'hydrodynamic'
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
    elif (submodelTitle == "constant_volume"):
        submodelTitle = "Constant Volume"
    elif (submodelTitle == "changing_volume"):
        submodelTitle = "Changing Volume"
    elif (submodelTitle == "kinematic_wave"):
        submodelTitle = "Kinematic Wave"
    return hydro_d.header + " - " + submodelTitle


def get_submodel_description(submodel):
    """
    Gets the submodel description.
    :param submodel: Current submodel
    :return: submodel description as a string
    """
    if (submodel == "overview"):
        return hydro_d.description
    elif (submodel == "constant_volume"):
        return hydro_d.constantvolume_description
    elif (submodel == "changing_volume"):
        return hydro_d.changingvolume_description
    elif (submodel == "kinematic_wave"):
        return hydro_d.kinematicwave_description
    else:
        return hydro_d.unknown_description


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
    html += render_to_string('04hms_mathjax.html', {})

    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    description = get_submodel_description(submodel)
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header,
        'TEXT_PARAGRAPH': description
    })
    html += render_to_string('07ubertext_end_drupal.html', {})

    #input_module = get_model_input_module(model)
    #input_page_func = getattr(input_module, model + '_input_page')
    #html += input_page_func(request, model, submodel, header)
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
