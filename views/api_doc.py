'''
HMS API Documentation
'''

from django.template.loader import render_to_string
from django.http import HttpResponse
import os
import json
import requests


def create_swagger_docs(request):
    url = "/hms/api_doc/swagger/"
    html = render_to_string('swagger/hms_swagger_index.html', {"URL": url})
    # html = render_to_string('hms_swagger_2.html', {"URL": url})
    response = HttpResponse()
    response.write(html)
    return response


def get_swagger_json(request):
    """
    Opens up swagger.json content
    """
    print("Swagger json request local: " + str(os.environ['HMS_LOCAL']))
    if os.environ['HMS_LOCAL'] == "True" and os.environ["IN_DOCKER"] == "False":
        url = "http://localhost:60050/swagger/v1/swagger.json"
    else:
        url = str(os.environ.get('HMS_BACKEND_SERVER_DOCKER')) + '/swagger/v1/swagger.json'
    print("Swagger json request url: " + url)
    protocol = "https" if "https" in request.META["HTTP_REFERER"] else "http"  #request.META["SERVER_PROTOCOL"].split("/")
    swagger = requests.get(url)
    swagger = json.loads(swagger.content)
    swagger["servers"] = [{"url": protocol + "://" + request.META["HTTP_HOST"] + "/hms/rest", "description": "HMS Frontend"}]
    response = HttpResponse()
    response.write(json.dumps(swagger))
    return response
