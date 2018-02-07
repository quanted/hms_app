from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
import json
import os
import requests


""" 
REST endpoints for HMS django frontend and proxy functions
"""


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
    if os.environ['HMS_LOCAL'] == "True":
        proxy_url = "http://localhost:60049/api/" + module
    else:
        proxy_url = os.environ.get('HMS_BACKEND_SERVER') + "/HMSWS/api/" + module
    method = str(request.method)
    print("HMS proxy: " + method + " url: " + proxy_url)
    if method == "POST":
        data = json.loads(request.body)
        hms_request = requests.request("post", proxy_url, json=data)
        return HttpResponse(hms_request, content_type="application/json")
    elif method == "GET":
        hms_request = requests.request("get", proxy_url)
        return HttpResponse(hms_request, content_type="application/json")
    else:
        print("Django to Flask proxy url invalid.")
        raise Http404
