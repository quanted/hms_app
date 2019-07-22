"""
HMS Workflow page setup functions
"""
import os
from django.http import HttpResponse
from django.template.loader import render_to_string
from .default_pages import build_model_page

from hms_app.models.workflow import water_quality_parameters as wqp


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
