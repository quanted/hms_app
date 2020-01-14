"""
HMS Workflow page setup functions
"""
import os
from django.http import HttpResponse
from django.template.loader import render_to_string
from .default_pages import build_model_page, build_map_model_page

from ..models.workflow import time_of_travel_overview as tot
from ..models.workflow import workflow_parameters as workflow


def water_quality_page(request):
    model = "workflow"
    submodel = "water_quality"
    title = "Water Quality Workflow"
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA"
    notpublic = True
    disclaimer_file = open(os.path.join(os.environ['PROJECT_PATH'], 'hms_app/views/disclaimer.txt'), 'r')
    disclaimer_text = disclaimer_file.read()

    import_block = render_to_string("workflow/water_quality_imports.html", {'SUBMODEL': submodel})

    html = render_to_string("workflow/water_quality_body.html")
    response = HttpResponse()
    response.write(html)
    return response


def time_of_travel_page(request):
    model = "workflow"
    submodel = "time_of_travel"
    title = "Time of Travel"
    import_block = render_to_string("workflow/time_of_travel_imports.html")
    p = request.scheme + "://" + request.get_host()
    details = tot.TimeOfTravel
    description = build_overview_page(p, submodel, details)

    input_form = workflow.TimeOfTravelFormInput()
    algorithm = render_to_string('hms_submodel_algorithms.html',
                                 {"ALGORITHMS": details.algorithms})
    input = render_to_string('04hms_input_form.html', {'FORM': input_form})
    input_block = render_to_string('04hms_precipcompare_input.html', {'INPUT': input})

    html = build_map_model_page(request=request, model=model, submodel=submodel, title=title, import_block=import_block,
                                description=description, input_block=input_block, algorithms=algorithm)
    response = HttpResponse()
    response.write(html)
    return response


def build_overview_page(base_url, submodel, details):
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
