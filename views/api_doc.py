'''
HMS API Documentation
'''

from django.template.loader import render_to_string
from django.http import HttpResponse
import os
import json
import requests


def create_swagger_docs(request):
    html = render_to_string('hms_swagger.html', {})
    response = HttpResponse()
    response.write(html)
    return response


def get_swagger_json(request):
    """
    Opens up swagger.json content
    """
    #url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/swagger/docs/v1'  # HMS backend server for swagger
    url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/swagger/v1/swagger.json'  # .NET core backend
    swagger = requests.get(url)
    swagger = json.loads(swagger.content)
    swagger["host"] = str(os.environ.get('HMS_BACKEND_SERVER'))  # changes internal ip to external ip
    # swagger["host"] = "134.67.114.8"
    # swagger["schemes"] = ["https"]
    response = HttpResponse()
    response.write(json.dumps(swagger))
    return response
