"""
Router to direct requests for a specified model/submodule
"""

from django.shortcuts import redirect
from .hydrology_submodels import submodel_page as hydrology_submodel
from .hydrodynamic_submodels import submodel_page as hydrodynamic_submodel
from .hydrodynamic_submodels_run import submodel_page as hydrodynamic_submodel_run
from .hydrodynamic_submodels_algorithms import submodel_page as hydrodynamic_submodel_algorithms
import logging

hydrology_submodules = ["evapotranspiration", "soilmoisture", "surfacerunoff"]
hydrodynamic_modules = ['overview', "constant_volume", "changing_volume", "kinematic_wave"]
meteorology_submodules = ["precipitation", "solarcalculator", "temperature"]

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

    if model == "hydrology":
        if submodule in hydrology_submodules:
            # construct page from existing code
            landing_html = hydrology_submodel(request, submodule)
        else:
            # redirect to default hms/hydrology page, invalid submodule request
            return redirect('/hms/hydrology/')
    elif model == "hydrodynamic":
        if submodule in hydrodynamic_modules:
            # construct page for hydrodynamic submodule
            landing_html = hydrodynamic_submodel(request, submodule)
            #run
        else:
            # redirect to default hms/hydrodynamics page, invalid submodule request
            return redirect('/hms/hydrodynamic/')
    elif model == "meteorology":
        if submodule in meteorology_submodules:
            # construct page for meteorlogy submodules
            # (will need some recoding due to some submodules existing in hydrology_submodels)
            landing_html = "stuff"
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

    if model == "hydrology":
        if submodule in hydrology_submodules:
            # construct page from existing code
            run_html = hydrology_submodel(request, submodule)
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
            run_html = "stuff"
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

    if model == "hydrology":
        if submodule in hydrology_submodules:
            # construct page from existing code
            run_html = hydrology_submodel(request, submodule)
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
            # construct page for meteorlogy submodules
            # (will need some recoding due to some submodules existing in hydrology_submodels)
            run_html = "stuff"
        else:
            # redirect to default hms/meteorology page, invalid submodule request
            return redirect('/hms/meteorology/')
    else:
        # redirect to default hms page, invalid model request
        return redirect('/hms/')
    return algorithm_html