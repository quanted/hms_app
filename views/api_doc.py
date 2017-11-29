'''
HMS API Documentation
'''

from django.template.loader import render_to_string
from django.http import HttpResponse
import os
import json
import requests


def create_swagger_docs(request):
    url = "/hms/api_doc/swagger"
    html = render_to_string('hms_swagger_2.html', {"URL": url})
    response = HttpResponse()
    response.write(html)
    return response


def get_swagger_json(request):
    """
    Opens up swagger.json content
    """
    if os.environ['HMS_LOCAL'] == "True":
        url = "http://localhost:60049/swagger/v1/swagger.json"
    else:
        #url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/swagger/docs/v1'  # HMS backend server for swagger
        url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/swagger/v1/swagger.json'  # .NET core backend
    swagger = requests.get(url)
    swagger = json.loads(swagger.content)
    if os.environ['HMS_LOCAL'] == "True":
        # swagger["host"] = "localhost:60049"
        swagger["host"] = "localhost:7777/hms"
    else:
        # swagger["host"] = str(os.environ.get('HMS_BACKEND_SERVER'))  # changes internal ip to external ip
        swagger["host"] = "qedinternal.epa.gov/hms"
        # swagger["host"] = "134.67.114.8"
    # swagger["schemes"] = ["https"]
    response = HttpResponse()
    response.write(json.dumps(swagger))
    return response
