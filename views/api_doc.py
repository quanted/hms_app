'''
HMS API Documentation
'''

from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
import hms_app.views.links_left as links_left
import os
import json
import requests


def create_swagger_docs(request):
    url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/swagger/docs/v1'  # HMS backend server for swagger
    # TODO: Create package for generating Swagger-UI page from pre-existing JSON
    # CURRENTLY: Copying cts and hwbi swagger pages, static template files.
    error = ""
    file_path = os.path.join(os.path.dirname(__file__), "..", "..", "static_qed")
    try:
        swagger = requests.get(url)
        swagger = json.loads(swagger.content)
        f = open(file_path + '/hms/json/hms_swagger.json', 'w')
        f.write(json.dumps(swagger))
        f.close()
    except FileNotFoundError as e:
        error = "Swagger Error: Failed to open swagger json configuration file."
    if "Swagger Error" in error:
        html = render_to_string('01epa_drupal_header.html', {
            'SITE_SKIN': os.environ['SITE_SKIN'],
            'TITLE': "HMS Swagger Documentation"
        })
        html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
        html += render_to_string('03epa_drupal_section_title.html', {})
        html += render_to_string('06ubertext_start_index_drupal.html', {
            'TITLE': "HMS Swagger Documentation",
            'TEXT_PARAGRAPH': error
        })
        html += render_to_string('07ubertext_end_drupal.html', {})
        html += links_left.ordered_list("api_doc", submodel=None)

        html += render_to_string('09epa_drupal_splashscripts.html', {})
        html += render_to_string('10epa_drupal_footer.html', {})
    else:
        html = render_to_string('hms_swagger.html', {})
    response = HttpResponse()
    response.write(html)
    return response


def getSwaggerJsonContent(request):
    """
    Opens up swagger.json content
    """
    file_path = os.path.join(os.path.dirname(__file__), "..", "..", "static_qed")
    swag = open(file_path + '/hms/json/hms_swagger.json', 'r').read()
    swag_filtered = swag.replace('\n', '').strip()
    swag_obj = json.loads(swag_filtered)
    response = HttpResponse()
    response.write(json.dumps(swag_obj))
    return response
