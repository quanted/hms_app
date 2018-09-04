"""
HMS Runoff Comparision page functions
"""

from django.http import HttpResponse
from django.template.loader import render_to_string
import hms_app.views.links_left as links_left
import hms_app.models.runoff_compare.views as runoff_compare_view
import hms_app.models.currently_in_development as cid


def input_page(request, header='none'):
    """
    Constructs complete input page for runoff compare
    :param request: current request object
    :param header: current header set to none
    :return: HttpResponse object
    """
    header = runoff_compare_view.header
    html = build_page(request, "runoff_compare", header)
    response = HttpResponse()
    response.write(html)
    return response

def build_page(request, model, header):
    """
    Constructs html for runoff compare page
    :param request: current request object
    :param model: current model
    :param header: current header
    :return: string formatted as html
    """
    page_title = "HMS: Runoff Data Compare"
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA, Precipitation, Precipitation Compare"
    imports = render_to_string('hms_default_imports.html')

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Work Flows",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports
    })                                                                     # Default EPA header
    html += links_left.ordered_list(model=model, submodel=None)
    description = cid.currently_in_development_page(request, model=model, header=header)
    html += render_to_string('05hms_body_start.html', {
        'TITLE': page_title,
        'TEXT_PARAGRAPH': description
    })

    html += render_to_string('06hms_body_end.html')
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    return html
