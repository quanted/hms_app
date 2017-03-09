from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import links_left
import os
#import secret
from django.conf import settings


def hms_landing_page(request):
    page_text_file = open(os.path.join(os.environ['PROJECT_PATH'], 'hms_app/views/landing_text.txt'), 'r')
    page_text = page_text_file.read()

    """ Returns the html of the landing page for qed. """
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS"
    })
    #html += render_to_string('02epa_drupal_header_bluestripe.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    #Page Content
    if settings.IS_PUBLIC:
        pass
    else:
        html += render_to_string('06ubertext_start_index_drupal.html',{
            'TITLE': 'Hydrologic Micro Services',
            'TEXT_PARAGRAPH': page_text
        })
    # Left side links
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model='hms')

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
