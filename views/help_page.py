from django.http import HttpResponse
from django.template.loader import render_to_string
import hms_app.views.links_left as links_left
import json
import os


def help_page(request):
    """
    :param request:
    :return:
    """
    page_title = "HMS: Hydrologic Micro Services"
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA"
    imports = render_to_string('hms_default_imports.html')
    imports += render_to_string('hms_help_import.html')
    html = render_to_string('01epa18_default_header.html', {
        'TITLE': page_title,
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports,
        'NOTPUBLIC': False,
        'DISCLAIMER': None
    })                                                                     # Default EPA header
    html += links_left.ordered_list(model='documentation', submodel='help')
    faq_path = os.path.join(os.environ['PROJECT_PATH'], 'hms_app', 'views', 'help_faq.json')
    with open(faq_path) as f:
        faq = json.load(f)
    page_text = render_to_string("04hms_help_body.html", {'FAQ': faq}, request=request)

    html += render_to_string('05hms_body_start.html', {
        'TITLE': "HMS Help",
        'DESCRIPTION': page_text
    })                                                                      # HMS Workflow main body start
    html += render_to_string('06hms_body_end.html')                         # HMS Workflow main body end
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    response = HttpResponse()
    response.write(html)
    return response