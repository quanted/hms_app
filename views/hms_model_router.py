"""
Router to direct requests for a specified model/submodule
"""

from . import meteorology_submodels as met_submodels
from . import meteorology_submodels_algorithms as met_submodel_algor
from django.http import HttpResponse
from django.template.loader import render_to_string
import hms_app.views.links_left as links_left


from django.shortcuts import redirect
from .hydrology_submodels import submodel_page as hydrology_submodel
from .v2hydrology_submodels import submodel_page as v2hydrology_submodel
from .meteorology_submodels import submodel_page as meteorology_submodel
from .hydrodynamic_submodels import submodel_page as hydrodynamic_submodel
from .hydrology_submodels_run import submodel_page as hydrology_submodel_run
from .meteorology_submodels_run import submodel_page as meteorology_submodel_run
from .hydrodynamic_submodels_run import submodel_page as hydrodynamic_submodel_run
from .hydrodynamic_submodels_algorithms import submodel_page as hydrodynamic_submodel_algorithms
from .meteorology_submodels_algorithms import submodel_page as meteorology_submodel_algorithms
from .hydrology_submodels_algorithms import submodel_page as hydrology_submodel_algorithms
from .hydrodynamic_submodels_output import hydrodynamics_output_page as hydrodynamics_output_page
from .meteorology_submodels_output import meteorology_output_page as meteorology_output_page
from .hydrology_submodels_output import v2hydrology_output_page as hydrology_output_page
import logging

hydrology_submodules = ['overview', "evapotranspiration", "soilmoisture", "surfacerunoff", "subsurfaceflow"]
hydrodynamic_modules = ['overview', "constant_volume", "changing_volume", "kinematic_wave"]
meteorology_submodules = ['overview', "precipitation", "solarcalculator", "temperature"]


def component_page(request, model, submodel):
    """
    Build the component page for the model/submodel
    :param request:
    :param model:
    :param submodel:
    :return:
    """
    model = str(model).lower()
    submodel = str(submodel).lower()
    logging.info("hms page request, model: " + model + "; submodel: " + submodel)
    print("hms page request, model: " + model + "; submodel: " + submodel)

    description = ""
    input_block = ""
    algorithm = ""
    title = "{} - {}".format(model.capitalize(), submodel.capitalize())
    import_block = None

    if model == "meteorology":
        description = met_submodels.get_submodel_description(submodel)
        if submodel == "overview":
            input_block = None
            algorithm = None
        elif submodel == "precipitation":
            import_block = render_to_string("{}/{}_imports.html".format(model, submodel))
            input_model = met_submodels.get_model_input_module(model)
            input_page_func = getattr(input_model, 'get_submodel_form_input')
            input_form = input_page_func(submodel, None)
            input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
            algorithm = met_submodel_algor.get_submodel_description(submodel)
        elif submodel == "temperature":
            import_block = render_to_string("{}/{}_imports.html".format(model, submodel))
            input_model = met_submodels.get_model_input_module(model)
            input_page_func = getattr(input_model, 'get_submodel_form_input')
            input_form = input_page_func(submodel, None)
            input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
            algorithm = met_submodel_algor.get_submodel_description(submodel)
        elif submodel == "solarcalculator":
            import_block = render_to_string("{}/{}_imports.html".format(model, submodel))
            input_model = met_submodels.get_model_input_module(model)
            input_page_func = getattr(input_model, 'get_submodel_form_input')
            input_form = input_page_func(submodel, None)
            input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
            algorithm = met_submodel_algor.get_submodel_description(submodel)
        else:
            return error_404_page(request)

    html = build_model_page(request, model, submodel, title, import_block, description, input_block, algorithm)
    response = HttpResponse()
    response.write(html)
    return response


def build_model_page(request, model, submodel, title=None, import_block=None, description=None, input_block=None, algorithms=None):
    """
    Compiles model/submodel page for hms
    :param request:
    :param model:
    :param submodel:
    :param title:
    :param import_block:
    :param description:
    :param input_block:
    :param algorithms:
    :return:
    """
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA"
    imports = render_to_string('hms_default_imports.html')
    if import_block is not None:
        imports += import_block

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Hydrologic Micro Services",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports
    })
    html += links_left.ordered_list(model=model, submodel=submodel)
    if input_block is None and algorithms is None:
        html += render_to_string('05hms_body_start.html', {
            'TITLE': title,
            'DESCRIPTION': description
        })
    else:
        html += render_to_string('05hms_body_start_2.html', {
            'TITLE': title,
            'DESCRIPTION': description,
            'INPUT_FORM': input_block,
            'ALGORITHMS': algorithms
        })
    html += render_to_string('06hms_body_end.html')
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    return html


def error_404_page(request):
    """
    Compiles model/submodel page for hms
    :param request:
    :param model:
    :param submodel:
    :param title:
    :param import_block:
    :param description:
    :param input_block:
    :param algorithms:
    :return:
    """
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA"
    imports = render_to_string('hms_default_imports.html')
    description = "The requested page was not found."
    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Hydrologic Micro Services",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports
    })
    html += links_left.ordered_list(model="", submodel="")
    html += render_to_string('05hms_body_start.html', {
        'TITLE': "Page Not Found",
        'DESCRIPTION': description
    })
    html += render_to_string('06hms_body_end.html')
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    response = HttpResponse()
    response.write(html)
    return response


def landing_page(request, model, submodule):
    """
    Redirect to the appropriate model and submodule of the request.
    :param request: Request object
    :param model: Requested model
    :param submodule: Requested submodule
    :return: Constructed page
    """
    model = str(model).lower()
    submodule = str(submodule).lower()
    logging.info("hms page request, model: " + model + "; submodule: " + submodule)
    print("hms page request, model: " + model + "; submodule: " + submodule)

    if model == "v2hydrology":
        if submodule in hydrology_submodules:
            # construct page from existing code
            landing_html = v2hydrology_submodel(request, submodule)
        else:
            # redirect to default hms/hydrology page, invalid submodule request
            return redirect('/hms/v2hydrology/')
    elif model == "hydrodynamic":
        if submodule in hydrodynamic_modules:
            # construct page for hydrodynamic submodule
            landing_html = hydrodynamic_submodel(request, submodule)
        else:
            # redirect to default hms/hydrodynamics page, invalid submodule request
            return redirect('/hms/hydrodynamic/')
    elif model == "hydrology":
        if submodule in hydrology_submodules:
            # construct page from existing code
            landing_html = hydrology_submodel(request, submodule)
        else:
            # redirect to default hms/hydrology page, invalid submodule request
            return redirect('/hms/hydrology/')
    elif model == "meteorology":
        if submodule in meteorology_submodules:
            # construct page for meteorlogy submodules
            # (will need some recoding due to some submodules existing in hydrology_submodels)
            landing_html = meteorology_submodel(request, submodule)
        else:
            # redirect to default hms/meteorology page, invalid submodule request
            return redirect('/hms/meteorology/')
    else:
        # redirect to default hms page, invalid model request
        return redirect('/hms/')
    return landing_html


def run(request, model, submodule):
    """
    Redirect to the appropriate model and submodule of the request.
    :param request: Request object
    :param model: Requested model
    :param submodule: Requested submodule
    :return: Constructed page
    """
    model = str(model).lower()
    submodule = str(submodule).lower()
    logging.info("hms page request, model: " + model + "; submodule: " + submodule)
    print("hms page request, model: " + model + "; submodule: " + submodule)

    if model == "v2hydrology":
        if submodule in hydrology_submodules:
            # construct page from existing code
            run_html = hydrology_submodel_run(request, submodule)
        else:
            # redirect to default hms/hydrology page, invalid submodule request
            return redirect('/hms/hydrology/')
    elif model == "hydrodynamic":
        if submodule in hydrodynamic_modules:
            # construct page for hydrodynamic submodule
            run_html = hydrodynamic_submodel_run(request, submodule)

        else:
            # redirect to default hms/hydrodynamics page, invalid submodule request
            return redirect('/hms/hydrodynamic/')
    elif model == "meteorology":
        if submodule in meteorology_submodules:
            # construct page for meteorlogy submodules
            # (will need some recoding due to some submodules existing in hydrology_submodels)
            run_html = meteorology_submodel_run(request, submodule)
        else:
            # redirect to default hms/meteorology page, invalid submodule request
            return redirect('/hms/meteorology/')
    else:
        # redirect to default hms page, invalid model request
        return redirect('/hms/')
    return run_html


def algorithms(request, model, submodule):
    """
    Redirect to the appropriate model and submodule of the request.
    :param request: Request object
    :param model: Requested model
    :param submodule: Requested submodule
    :return: Constructed page
    """
    model = str(model).lower()
    submodule = str(submodule).lower()
    logging.info("hms page request, model: " + model + "; submodule: " + submodule)
    print("hms page request, model: " + model + "; submodule: " + submodule)

    if model == "v2hydrology":
        if submodule in hydrology_submodules:
            # construct page from existing code
            algorithm_html = hydrology_submodel_algorithms(request, submodule)
        else:
            # redirect to default hms/hydrology page, invalid submodule request
            return redirect('/hms/hydrology/')
    elif model == "hydrodynamic":
        if submodule in hydrodynamic_modules:
            # construct page for hydrodynamic submodule
            algorithm_html = hydrodynamic_submodel_algorithms(request, submodule)

        else:
            # redirect to default hms/hydrodynamics page, invalid submodule request
            return redirect('/hms/hydrodynamic/')
    elif model == "meteorology":
        if submodule in meteorology_submodules:
            # construct page for meteorology submodules
            # (will need some recoding due to some submodules existing in hydrology_submodels)
            algorithm_html = meteorology_submodel_algorithms(request, submodule)
        else:
            # redirect to default hms/meteorology page, invalid submodule request
            return redirect('/hms/meteorology/')
    else:
        # redirect to default hms page, invalid model request
        return redirect('/hms/')
    return algorithm_html


def output(request, model, submodule):
    """
    Redirect to the appropriate model and submodule of the request.
    :param request: Request object
    :param model: Requested model
    :param submodule: Requested submodule
    :return: Constructed page
    """
    model = str(model).lower()
    submodule = str(submodule).lower()
    logging.info("hms page request, model: " + model + "; submodule: " + submodule)
    print("hms page request, model: " + model + "; submodule: " + submodule)

    if model == "v2hydrology":
        if submodule in hydrology_submodules:
            # construct page from existing code
            output_html = hydrology_output_page(request, submodule)
        else:
            # redirect to default hms/hydrology page, invalid submodule request
            return redirect('/hms/hydrology/')
    elif model == "hydrodynamic":
        if submodule in hydrodynamic_modules:
            # construct page for hydrodynamic submodule
            output_html = hydrodynamics_output_page(request, submodel=submodule)
        else:
            # redirect to default hms/hydrodynamics page, invalid submodule request
            return redirect('/hms/hydrodynamic/')
    elif model == "meteorology":
        if submodule in meteorology_submodules:
            # construct page for meteorlogy submodules
            # (will need some recoding due to some submodules existing in hydrology_submodels)
            output_html = meteorology_output_page(request, submodel=submodule)
        else:
            # redirect to default hms/meteorology page, invalid submodule request
            return redirect('/hms/meteorology/')
    else:
        # redirect to default hms page, invalid model request
        return redirect('/hms/')
    return output_html
