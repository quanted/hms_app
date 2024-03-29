"""
Router to direct requests for a specified model/submodule overview
"""

from . import meteorology_submodels as met_submodels
from . import hydrology_submodels as hydro_submodels
from . import hydrology_submodels_algorithms as hydro_submodel_algor
import hms_app.models.precip_workflow.precip_compare_overview as precip_compare
import hms_app.models.precip_workflow.precip_extraction_overview as precip_extract
import hms_app.models.precip_workflow.precip_compare_parameters as pcp
import hms_app.models.workflow.workflow_overview as workflow
import hms_app.models.workflow.streamflow_overview as streamflow
import hms_app.models.workflow.time_of_travel_overview as tot
import hms_app.models.workflow.workflow_parameters as wk_parameters
from . import precip_compare_setup
from django.http import HttpResponse
from django.template.loader import render_to_string
from .default_pages import error_404_page, build_overview_page, build_input_page, build_algorithms_page, build_output_page
import logging

hydrology_submodules = ['overview', "evapotranspiration", "soilmoisture", "surfacerunoff", "subsurfaceflow"]
hydrodynamic_modules = ['overview', "constant_volume", "changing_volume", "kinematic_wave"]
meteorology_submodules = ['overview', "precipitation", "radiation", "solarcalculator", "temperature", "wind", "humidity"]


def get_overview(request, model=None, submodule=None):
    """
    Dynamically build the submodule overview page
    :param request:
    :param model:
    :param submodule:
    :return:
    """
    model = str(model).lower()
    submodule = str(submodule).lower()
    logging.info("hms page request, model: " + model + "; submodule: " + submodule)
    print("hms page request, model: " + model + "; submodule: " + submodule)

    title = "{} - {}".format(model.capitalize(), submodule.replace("_", " ").capitalize())
    p = request.scheme + "://" + request.get_host()
    import_block = None
    top = False
    if submodule == "overview":
        top = True
    if model == "meteorology":
        if submodule != "overview":
            import_block = render_to_string("{}/{}_imports.html".format(model, submodule))
        description = met_submodels.get_submodel_description(p, submodule)
    elif model == "hydrology":
        if submodule != "overview":
            import_block = render_to_string("{}/{}_imports.html".format(model, submodule))
        description = hydro_submodels.get_submodel_description(p, submodule)
    elif model == "workflow":
        if submodule == "streamflow":
            import_block = render_to_string('workflow/hms_workflow_imports.html')
            description = streamflow.Streamflow.description
        elif submodule == "time_of_travel":
            import_block = render_to_string("workflow/time_of_travel_imports.html")
            description = tot.TimeOfTravel.description
        elif submodule == "overview":
            description = workflow.Workflow.description
        else:
            import_block = render_to_string("workflow/precip_workflow_imports.html", {'SUBMODEL': submodule})
            description = precip_compare_setup.build_overview_page(p, submodule)
    else:
        return error_404_page(request)
    html = build_overview_page(request=request, model=model, submodule=submodule, title=title, import_block=import_block, description=description, top=top)
    response = HttpResponse()
    response.write(html)
    return response


def get_data_request(request, model=None, submodule=None):
    """
    Dynamically build the submodule data request page
    :param request:
    :param model:
    :param submodule:
    :return:
    """
    model = str(model).lower()
    submodule = str(submodule).lower()
    logging.info("hms page request, model: " + model + "; submodule: " + submodule)
    print("hms page request, model: " + model + "; submodule: " + submodule)

    title = "{} - {}".format(model.capitalize(), submodule.replace("_", " ").capitalize())
    if model == "meteorology":
        import_block = render_to_string("{}/{}_imports.html".format(model, submodule))
        input_model = met_submodels.get_model_input_module(model)
        input_page_func = getattr(input_model, 'get_submodel_form_input')
        input_form = input_page_func(submodule, None)
        input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
    elif model == "hydrology":
        import_block = render_to_string("{}/{}_imports.html".format(model, submodule))
        input_model = hydro_submodels.get_model_input_module(model)
        input_page_func = getattr(input_model, 'get_submodel_form_input')
        input_form = input_page_func(submodule, None)
        input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
    elif model == "workflow":
        import_block = render_to_string("workflow/precip_workflow_imports.html", {'SUBMODEL': submodule})
        if submodule == "precip_compare":
            input = render_to_string('04hms_input_form_v2.html')
            input_block = render_to_string('04hms_precipcompare_input.html', {'INPUT': input})
        elif submodule == "precip_data_extraction":
            input_form = pcp.PrecipitationCompareFormInput()
            input = render_to_string('04hms_input_form.html', {'FORM': input_form})
            input_block = render_to_string('04hms_precipcompare_input.html', {'INPUT': input})
        elif submodule == "streamflow":
            import_block = render_to_string('workflow/hms_workflow_imports.html')
            input_block = render_to_string('workflow/hms_workflow_input_body.html')
        elif submodule == "time_of_travel":
            import_block = render_to_string("workflow/time_of_travel_imports.html")
            input_form = wk_parameters.TimeOfTravelFormInput()
            input = render_to_string('04hms_input_form.html', {'FORM': input_form})
            # input_block = render_to_string('04hms_precipcompare_input.html', {'INPUT': input})
            input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
        else:
            return error_404_page(request)
    else:
        return error_404_page(request)
    html = build_input_page(request=request, model=model, submodule=submodule, title=title, import_block=import_block, input_block=input_block)
    response = HttpResponse()
    response.write(html)
    return response


def get_algorithms(request, model=None, submodule=None):
    """
    Dynamically build the submodule algorithms page
    :param request:
    :param model:
    :param submodule:
    :return:
    """
    model = str(model).lower()
    submodule = str(submodule).lower()
    logging.info("hms page request, model: " + model + "; submodule: " + submodule)
    print("hms page request, model: " + model + "; submodule: " + submodule)

    title = "{} - {}".format(model.capitalize(), submodule.replace("_", " ").capitalize())
    if model == "meteorology":
        import_block = render_to_string("{}/{}_imports.html".format(model, submodule))
        algorithms = render_to_string('hms_submodel_algorithms.html',
                                     {'ALGORITHMS': met_submodels.get_submodel_algorithm(submodule)})
    elif model == "hydrology":
        import_block = render_to_string("{}/{}_imports.html".format(model, submodule))
        algorithms = render_to_string('hms_submodel_algorithms.html',
                                     {'ALGORITHMS': hydro_submodel_algor.get_submodel_description(submodule)})
    elif model == "workflow":
        import_block = render_to_string("workflow/precip_workflow_imports.html", {'SUBMODEL': submodule})
        if submodule == "precip_compare":
            algorithms = render_to_string("hms_submodel_algorithms.html",
                                         {'ALGORITHMS': precip_compare.PrecipCompare.algorithms})
        elif submodule == "precip_data_extraction":
            algorithms = render_to_string('hms_submodel_algorithms.html',
                                         {"ALGORITHMS": precip_extract.PrecipExtract.algorithms})
        elif submodule == "streamflow":
            import_block = render_to_string('workflow/hms_workflow_imports.html')
            algorithms = render_to_string('hms_submodel_algorithms.html',
                                          {"ALGORITHMS":  streamflow.Streamflow.algorithms})
        elif submodule == "time_of_travel":
            import_block = render_to_string("workflow/time_of_travel_imports.html")
            algorithms = render_to_string('hms_submodel_algorithms.html',
                                         {"ALGORITHMS": tot.TimeOfTravel.algorithms})
        else:
            return error_404_page(request)
    else:
        return error_404_page(request)
    html = build_algorithms_page(request=request, model=model, submodule=submodule, title=title, import_block=import_block, algorithms=algorithms)
    response = HttpResponse()
    response.write(html)
    return response


def get_output_request(request, model=None, submodule=None, task_id=None):
    """
    Dynamically build the submodule output page
    :param request:
    :param model:
    :param submodule:
    :return:
    """
    model = str(model).lower()
    submodule = str(submodule).lower()
    logging.info("hms page request, model: " + model + "; submodule: " + submodule)
    print("hms page request, model: " + model + "; submodule: " + submodule)

    title = "{} - {}".format(model.capitalize(), submodule.replace("_", " ").capitalize())
    output_block = None
    advanced = False
    if model == "workflow":
        import_block = render_to_string("workflow/precip_workflow_imports.html", {'SUBMODEL': submodule})
        if submodule == "streamflow":
            import_block = render_to_string('workflow/hms_workflow_imports.html')
            output_block = render_to_string("workflow/hms_workflow_output_body.html")
            advanced = True
        elif submodule == "time_of_travel":
            import_block = render_to_string("workflow/time_of_travel_imports.html")
    else:
        import_block = render_to_string("{}/{}_imports.html".format(model, submodule))
    html = build_output_page(request=request, model=model, submodule=submodule, title=title, import_block=import_block, task_id=task_id, output_block=output_block, advanced=advanced)
    response = HttpResponse()
    response.write(html)
    return response
