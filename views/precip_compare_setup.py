"""
HMS Precipitation Comparision page functions
"""

from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
import hms_app.models.precip_workflow.views as precip_compare_view
import hms_app.models.precip_workflow.data_extraction_views as precip_extract_view
from hms_app.models.precip_workflow import precip_compare_parameters as pcp
import os
import importlib
import hms_app.views.links_left as links_left
from .default_pages import build_model_page
import hms_app.models.precip_workflow.precip_compare_overview as precip_compare
import hms_app.models.precip_workflow.precip_extraction_overview as precip_extract


def precip_compare_page(request):
    model = "workflow"
    submodel = "precip_compare"
    p = request.scheme + "://" + request.get_host()
    title = precip_compare_view.header
    import_block = render_to_string("workflow/precip_workflow_imports.html", {'SUBMODEL': submodel})
    description = build_overview_page(p, submodel)

    # input_model = get_model_input_module(submodel)
    input_form = pcp.PrecipitationCompareFormInput()
    # input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
    # algorithm = precip_compare_view.algorithm
    algorithm = render_to_string("hms_submodel_algorithms.html", {'ALGORITHMS': precip_compare.PrecipCompare.algorithms})
    input = render_to_string('04hms_input_form_v2.html')
    input_block = render_to_string('04hms_precipcompare_input.html', {'INPUT': input})

    html = build_model_page(request=request, model=model, submodel=submodel, title=title, import_block=import_block,
                            description=description, input_block=input_block, algorithms=algorithm)
    response = HttpResponse()
    response.write(html)
    return response


def precip_extraction_page(request):
    model = "workflow"
    submodel = "precip_data_extraction"
    title = precip_extract_view.header
    import_block = render_to_string("workflow/precip_workflow_imports.html", {'SUBMODEL': submodel})
    p = request.scheme + "://" + request.get_host()
    description = build_overview_page(p, submodel)

    # input_model = get_model_input_module(submodel)
    input_form = pcp.PrecipitationCompareFormInput()
    # input_block = render_to_string('04hms_input_form.html', {'FORM': input_form})
    # algorithm = precip_extract_view.algorithm
    algorithm = render_to_string('hms_submodel_algorithms.html', {"ALGORITHMS": precip_extract.PrecipExtract.algorithms})
    input = render_to_string('04hms_input_form.html', {'FORM': input_form})
    input_block = render_to_string('04hms_precipcompare_input.html', {'INPUT': input})

    html = build_model_page(request=request, model=model, submodel=submodel, title=title, import_block=import_block,
                            description=description, input_block=input_block, algorithms=algorithm)
    response = HttpResponse()
    response.write(html)
    return response


def build_overview_page(base_url, submodel):
    details = None
    if submodel == "precip_compare":
        details = precip_compare.PrecipCompare
        submodel = "Precipitation Comparison"
    elif submodel == "precip_data_extraction":
        details = precip_extract.PrecipExtract
        submodel = "Precipitation Data Extraction"
    html = render_to_string('hms_submodel_overview.html', {
        'SUBMODEL': submodel,
        'DESCRIPTION': details.description,
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