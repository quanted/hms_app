from django.template.loader import render_to_string
from django.http import HttpResponse
import hms_app.views.links_left as links_left
import os


def hms_workflow_page(request):
    page_title = "HMS: Hydrological Watershed Workflow"
    keywords = "HMS, Hydrology, Hydrologic Micro Services, Watershed, Watershed Workflow"
    imports = render_to_string('workflow/hms_workflow_imports.html')

    html = render_to_string('workflow/01epa18_default_header.html', {
        'TITLE': page_title,
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports
    })                                                                     # Default EPA header
    html += links_left.ordered_list(model='workflow', submodel='v2')         # QED-HMS links left
    body = render_to_string('workflow/hms_workflow_body.html')              # HMS Workflow main body
    html += render_to_string('workflow/05hms_workflow_start.html', {
        'TEXT_PARAGRAPH': body
    })                                                                      # HMS Workflow main body start
    html += render_to_string('workflow/06hms_workflow_end.html')            # HMS Workflow main body end
    html += render_to_string('workflow/07hms_splashscripts.html')           # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    response = HttpResponse()
    response.write(html)
    return response


def hms_map_page(request):
    # x = render_to_string('hms_watershed_map.html')
    x = render_to_string('hms_workflow_map.html')
    """ Returns the html of the landing page for qed. """
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS"
    })
    # html += render_to_string('02epa_drupal_header_bluestripe.html', {})
    html += render_to_string('02hms_header_bluestripe_onesidebar.html', {})
    # html += render_to_string('03epa_drupal_section_title.html', {})
    html += render_to_string('03hms_section_title.html', {})

    # html += render_to_string('04ubertext_start_index_drupal.html', {
    #     'TITLE': 'HMS Watershed Delineation',
    #     'TEXT_PARAGRAPH': x})

    html += render_to_string('04hms_start_drupal.html', {
        'TITLE': 'HMS Watershed Delineation',
        'TEXT_PARAGRAPH': x})

    html += render_to_string('04ubertext_end_drupal.html', {})

    # Left side links
    # html += render_to_string('07ubertext_end_drupal.html', {})
    # html += links_left.ordered_list(model='watershed', submodel='')
    html += links_left.ordered_list(model='workflow', submodel='')

    html += render_to_string('09epa_drupal_splashscripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    response = HttpResponse()
    response.write(html)
    return response
