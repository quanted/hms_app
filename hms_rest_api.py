from json import JSONDecodeError
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods, require_GET
from django.views.decorators.csrf import csrf_exempt
import json
import os
import requests


""" 
REST endpoints for HMS django frontend and proxy functions
"""

request_header = {"User-Agent": "Mozilla/5.0"}
timeout = 300

@require_GET
def delineate_watershed(request):
    request_query = request.GET.dict()
    latitude = request_query["latitude"]
    longitude = request_query["longitude"]
    url = "https://streamstats.usgs.gov/streamstatsservices/watershed.geojson?rcode=NY&xlocation={0}&ylocation={1}&crs=4326&includeparameters=false&includeflowtypes=false&includefeatures=true&simplify=true"\
        .format(longitude, latitude)
    data = requests.request(method="get", url=url)
    json_data = json.loads(data.content.decode('utf-8', "ignore"))
    return HttpResponse(content=json.dumps(json_data), content_type="application/json")


@csrf_exempt
def pass_through_proxy(request, module):
    if os.getenv('HMS_LOCAL', "True") == "True" and os.getenv("IN_DOCKER", "False") == "False":
        proxy_url = "http://localhost:60050/api/" + module
    else:
        proxy_url = str(os.getenv('HMS_BACKEND', 'hms-dotnetcore:80/')) + "api/" + module
    method = str(request.method)
    print("HMS proxy: " + method + " url: " + proxy_url)
    if method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except JSONDecodeError as e:
            return HttpResponse(
                {
                    "POST Data ERROR": "POST request body was not valid or the type specified was not json. Error message: " + str(e)
                }
            )
        hms_request = requests.request("post", proxy_url, json=data, timeout=timeout)
        return HttpResponse(hms_request, content_type="application/json")
    elif method == "GET":
        proxy_url += "?" + request.GET.urlencode()
        hms_request = requests.request("get", proxy_url, timeout=timeout, )
        return HttpResponse(hms_request, content_type="application/json")
    else:
        print("Django to Flask proxy url invalid.")
        raise HttpResponseNotAllowed

@csrf_exempt
@require_http_methods(["GET", "POST", "DELETE"])
def flask_proxy(request, flask_url):
    if os.getenv('HMS_LOCAL', "True") == "True" and os.getenv("IN_DOCKER", "False") == "False":
        proxy_url = "http://localhost:7777" + "/" + flask_url
    else:
        proxy_url = os.getenv('FLASK_SERVER', "hms-nginx:7777") + "/" + flask_url
    method = str(request.method)
    print(f"Docker: {os.getenv('IN_DOCKER', 'False')},Django to Flask proxy method: " + method + " url: " + proxy_url )
    if method == "POST":
        if len(request.POST) == 0:
            try:
                request_body = (request.body.decode("utf-8")).replace('\t', '').replace('\r\n', '')
                # print(f"TYPE1: {type(request_body)}")
                if type(request_body) == str:
                    data = json.loads(request_body)
                else:
                    data = request_body
            except JSONDecodeError as e:
                return HttpResponseBadRequest(content=f"{e}".encode("utf-8"))
        else:
            data = request.POST
        proxy_url = proxy_url + "/"
        flask_request = requests.request("post", proxy_url, json=data, timeout=timeout, headers=request_header)
        return HttpResponse(flask_request, content_type="application/json")
    elif method == "GET":
        proxy_url += "?" + request.GET.urlencode()
        flask_request = requests.request("get", proxy_url, timeout=timeout)
        headers = flask_request.headers
        del headers["Content-Type"]
        response_type = flask_request.headers.get('content-type')
        if not response_type:
            response_type = "application/json"
        return HttpResponse(flask_request, content_type=response_type, headers=headers)
    elif method == "DELETE":
        proxy_url += "/?" + request.GET.urlencode()
        flask_request = requests.request("delete", proxy_url, timeout=timeout)
        return HttpResponse(flask_request, content_type="application/json")
    else:
        print("Django to Flask proxy url invalid.")
        raise HttpResponseNotAllowed

@csrf_exempt
@require_http_methods(["POST", "GET"])
def flask_proxy_v3(request, model):
    if os.getenv('HMS_LOCAL', "True") == "True" and os.getenv("IN_DOCKER", "False") == "False":
        proxy_url = "http://localhost:7777" + "/hms/proxy/" + model
    else:
        proxy_url = os.getenv('FLASK_SERVER', "hms-nginx:7777") + "/proxy/" + model
    method = str(request.method)
    print("Django to Flask proxy method: " + method + " url: " + proxy_url)
    if method == "POST":
        if len(request.POST) == 0:
            try:
                data = json.loads(request.body)
            except JSONDecodeError:
                return HttpResponseBadRequest()
        else:
            data = request.POST
        proxy_url = proxy_url + "/"
        flask_request = requests.request("post", proxy_url, json=data, timeout=timeout, headers=request_header)
        return HttpResponse(flask_request, content_type="application/json")
    else:
        print("Django to Flask proxy url invalid.")
        raise HttpResponseNotAllowed
