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
    html = render_to_string('hms_swagger.html', {})
    response = HttpResponse()
    response.write(html)
    return response


def getSwaggerJsonContent(request):
    """
    Opens up swagger.json content
    """
    url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/swagger/docs/v1'  # HMS backend server for swagger
    swagger = requests.get(url)
    swagger = json.loads(swagger.content)
    response = HttpResponse()
    response.write(json.dumps(swagger))
    return response
