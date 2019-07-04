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


# @ensure_csrf_cookie
# def input_page(request, header='none'):
#     """
#     Constructs complete input page for precip compare
#     :param request: current request object
#     :param header: current header set to none
#     :return: HttpResponse object
#     """
#     header = precip_compare_view.header
#     html = build_page(request, "precip_compare", header)
#     response = HttpResponse()
#     response.write(html)
#     return response


# def build_page(request, model, header):
#     """
#     Constructs html for precip compare page
#     :param request: current request object
#     :param model: current model
#     :param header: current header
#     :return: string formatted as html
#     """
#     page_title = "HMS: Precipitation Data Compare"
#     keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA, Precipitation, Precipitation Compare"
#     imports = render_to_string('hms_default_imports.html')
#
#     html = render_to_string('01epa18_default_header.html', {
#         'TITLE': "HMS: Work Flows",
#         'URL': str(request.get_host) + request.path,
#         'KEYWORDS': keywords,
#         'IMPORTS': imports
#     })                                                                     # Default EPA header
#     html += links_left.ordered_list(model=model, submodel=None)
#     description = get_description(model)
#     html += render_to_string('05hms_body_start.html', {
#         'TITLE': page_title,
#         'TEXT_PARAGRAPH': description
#     })
#     input_module = get_model_input_module(model)
#     input_page_func = getattr(input_module, model + '_input_page')
#     html += input_page_func(request, model)
#
#     html += render_to_string('06hms_body_end.html')
#     html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
#     html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
#     return html
#
#
# def build_page_old(request, model, header):
#     """
#     Constructs html for precip compare page
#     :param request: current request object
#     :param model: current model
#     :param header: current header
#     :return: string formatted as html
#     """
#     html = render_to_string('01epa_drupal_header.html', {
#         'SITE_SKIN': os.environ['SITE_SKIN'],
#         'TITLE': "HMS " + model
#     })
#     html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
#     html += render_to_string('03epa_drupal_section_title.html', {})
#     description = get_description(model)
#     html += render_to_string('06ubertext_start_index_drupal.html', {
#         'TITLE': header,
#         'TEXT_PARAGRAPH': description
#     })
#     html += render_to_string('07ubertext_end_drupal.html', {})
#
#     input_module = get_model_input_module(model)
#     input_page_func = getattr(input_module, model + '_input_page')
#     html += input_page_func(request, model)
#     html += links_left.ordered_list(model, "")
#
#     html += render_to_string('09epa_drupal_ubertool_css.html', {})
#     html += render_to_string('10epa_drupal_footer.html', {})
#     return html


# def get_model_input_module(model):
#     """
#     Gets the model input module for the input form.
#     :param model: current model
#     :return: input form object
#     """
#     model_module_location = 'hms_app.models.' + model + '.' + model + '_inputs'
#     model_input_module = importlib.import_module(model_module_location)
#     return model_input_module


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