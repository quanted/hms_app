from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import hms_app.views.links_left as links_left
import os
#import secret
from django.conf import settings


def hms_map_page(request):
    x = render_to_string('hms_watershed_map.html')

    """ Returns the html of the landing page for qed. """
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS"
    })
    # html += render_to_string('02epa_drupal_header_bluestripe.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': 'Watershed Delineation',
        'TEXT_PARAGRAPH': x})

    html += render_to_string('04ubertext_end_drupal.html', {})


    # Left side links
    # html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model='watershed', submodel='')

    html += render_to_string('09epa_drupal_splashscripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    response = HttpResponse()
    response.write(html)
    return response


def file_not_found(request):
    """ Returns the html of the landing page for qed. """
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
