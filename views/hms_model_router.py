"""
Router to direct requests for a specified model/submodule
"""

from . import meteorology_submodels as met_submodels
from . import meteorology_submodels_algorithms as met_submodel_algor
from . import hydrology_submodels as hydro_submodels
from . import hydrology_submodels_algorithms as hydro_submodel_algor
from django.http import HttpResponse
from django.template.loader import render_to_string
from .default_pages import build_model_page, error_404_page
import logging

hydrology_submodules = ['overview', "evapotranspiration", "soilmoisture", "surfacerunoff", "subsurfaceflow"]
hydrodynamic_modules = ['overview', "constant_volume", "changing_volume", "kinematic_wave"]
meteorology_submodules = ['overview', "precipitation", "solarcalculator", "temperature"]


def component_page(request, model=None, submodel=None):
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
            title = "{} - Solar Calculator".format(model.capitalize())
            import_block = render_to_string("{}/{}_imports.html".format(model, submodel))
            input_model = met_submodels.get_model_input_module(model)
            input_page_func = getattr(input_model, 'get_submodel_form_input')
            input_form = input_page_func(submodel, None)
            input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
            algorithm = met_submodel_algor.get_submodel_description(submodel)
        else:
            return error_404_page(request)
    elif model == "hydrology":
        description = hydro_submodels.get_submodel_description(submodel)
        if submodel == "overview":
            input_block = None
            algorithm = None
        elif submodel == "evapotranspiration":
            import_block = render_to_string("{}/{}_imports.html".format(model, submodel))
            input_model = hydro_submodels.get_model_input_module(model)
            input_page_func = getattr(input_model, 'get_submodel_form_input')
            input_form = input_page_func(submodel, None)
            input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
            algorithm = hydro_submodel_algor.get_submodel_description(submodel)
        elif submodel == "soilmoisture":
            title = "{} - Soil Moisture".format(model.capitalize())
            import_block = render_to_string("{}/{}_imports.html".format(model, submodel))
            input_model = hydro_submodels.get_model_input_module(model)
            input_page_func = getattr(input_model, 'get_submodel_form_input')
            input_form = input_page_func(submodel, None)
            input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
            algorithm = hydro_submodel_algor.get_submodel_description(submodel)
        elif submodel == "surfacerunoff":
            import_block = render_to_string("{}/{}_imports.html".format(model, submodel))
            input_model = hydro_submodels.get_model_input_module(model)
            input_page_func = getattr(input_model, 'get_submodel_form_input')
            input_form = input_page_func(submodel, None)
            input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
            algorithm = hydro_submodel_algor.get_submodel_description(submodel)
        elif submodel == "subsurfaceflow":
            import_block = render_to_string("{}/{}_imports.html".format(model, submodel))
            input_model = hydro_submodels.get_model_input_module(model)
            input_page_func = getattr(input_model, 'get_submodel_form_input')
            input_form = input_page_func(submodel, None)
            input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
            algorithm = hydro_submodel_algor.get_submodel_description(submodel)
        else:
            return error_404_page(request)
    else:
        return error_404_page(request)
    html = build_model_page(request=request, model=model, submodel=submodel, title=title, import_block=import_block,
                            description=description, input_block=input_block, algorithms=algorithm)
    response = HttpResponse()
    response.write(html)
    return response
