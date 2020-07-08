"""
HMS Landing page functions
"""

from django.template.loader import render_to_string
from django.http import HttpResponse
import hms_app.views.links_left as links_left
import os
from django.conf import settings


def hms_landing_page(request):
    page_title = "HMS: Hydrologic Micro Services"
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA"
    imports = render_to_string('hms_default_imports.html')

    disclaimer_file = open(os.path.join(os.environ['PROJECT_PATH'], 'hms_app/views/disclaimer.txt'), 'r')
    disclaimer_text = disclaimer_file.read()
    notpublic = True

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': page_title,
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports,
        'NOTPUBLIC': notpublic,
        'DISCLAIMER': disclaimer_text
    })                                                                     # Default EPA header
    html += links_left.ordered_list(model='hms', submodel=None)
    # page_text_file = open(os.path.join(os.environ['PROJECT_PATH'], 'hms_app/views/landing_text.txt'), 'r')
    page_text = render_to_string("hms_landing_body.html")

    html += render_to_string('05hms_body_start.html', {
        'TITLE': "HMS Introduction",
        'DESCRIPTION': page_text
    })                                                                      # HMS Workflow main body start
    html += render_to_string('06hms_body_end.html')                         # HMS Workflow main body end
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    response = HttpResponse()
    response.write(html)
    return response


def hms_landing_page_old(request):
    """
    DEPRECATED
    Constucts landing page html.
    :param request: current request object
    :return: HttpResponse object
    """
    page_text_file = open(os.path.join(os.environ['PROJECT_PATH'], 'hms_app/views/landing_text.txt'), 'r')
    page_text = page_text_file.read()

    """ Returns the html of the landing page for qed. """
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS"
    })
    page_title = "HMS: Hydrological Micro Services"
    keywords = "HMS, Hydrology, Hydrologic Micro Services, Watershed, Watershed Workflow"
    imports = render_to_string("hms_default_imports.html")

    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    # Page Content
    if settings.IS_PUBLIC:
        pass
    else:
        html += render_to_string('06ubertext_start_index_drupal.html',{
            'TITLE': page_title,
            'TEXT_PARAGRAPH': page_text
        })
    # Left side links
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model='hms', submodel=None)

    html += render_to_string('09epa_drupal_splashscripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    response = HttpResponse()
    response.write(html)
    return response


def file_not_found(request, exception=None):
    """
    Constructs html for page not found.
    :param request: current request object
    :return: HttpResponse object
    """
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})
    if settings.IS_PUBLIC:
        html += render_to_string('04qed_splash_landing_public.html', {'title': 'qed'})
    else:
        html += render_to_string('04qed_splash_landing_intranet.html', {'title': 'qed'})
    html += render_to_string('09epa_drupal_splashscripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    response = HttpResponse()
    response.write(html)
    print("page not found")
    return response
