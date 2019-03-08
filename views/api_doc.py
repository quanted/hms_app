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
    html = render_to_string('hms_swagger_2.html', {"URL": url})
    response = HttpResponse()
    response.write(html)
    return response


def get_swagger_json(request):
    """
    Opens up swagger.json content
    """
    print("Swagger json request local: " + str(os.environ['HMS_LOCAL']))
    if os.environ['HMS_LOCAL'] == "True":
        url = "http://localhost:60050/swagger/v1/swagger.json"
    else:
        # url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/swagger/v1/swagger.json'  # .NET core backend
        url = str(os.environ.get('HMS_BACKEND_SERVER_DOCKER')) + '/swagger/v1/swagger.json'
        # url = str(os.environ.get('HMS_BACKEND_SERVER_DOCKER')) + '/HMSWS/swagger/v1/swagger.json'
    print("Swagger json request url: " + url)
    swagger = requests.get(url)
    swagger = json.loads(swagger.content)
    if os.environ['HMS_LOCAL'] == "True":
        swagger["host"] = "127.0.0.1:8000/hms/rest"
        print("HMS Local")
    elif os.environ['HMS_BACKEND_SERVER_DOCKER'] == "http://172.16.0.4:7778":
        swagger["host"] = "172.16.0.4/hms/rest"
        swagger["basePath"] = ""
        print("HMS AZURE Backend Docker")
    elif os.environ['HMS_BACKEND_SERVER_DOCKER'] == "http://172.20.100.15:7778":
        swagger["host"] = "134.67.114.5/hms/rest"
        swagger["basePath"] = ""
        print("HMS CGI server 5")
    # elif os.environ['IN_DOCKER'] == "True":
    #     swagger["host"] = "172.20.100.11/hms/rest/"
    #     swagger["basePath"] = ""
    else:
        swagger["host"] = "qedinternal.epa.gov/hms/rest"
        swagger["basePath"] = ""
        print("HMS qedinteral")
    response = HttpResponse()
    response.write(json.dumps(swagger))
    return response
