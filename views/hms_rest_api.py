from django.http import HttpResponse, Http404
import json, requests


### Incomplete code
### began as an alternative to the flask script.
### TO be deleted if flask method adequate

# generic pass through method of WSHMS POST request
def pass_to_hms(request):
    print("pass_to_hms request passed")
    #url = 'http://134.67.114.8/HMSWS/api/WSHMS/'
    url = 'http://localhost:50052/api/WSHMS/'
    result = requests.post(url, body=request.body, timeout=1000)
    response = HttpResponse()
    HttpResponse.content = json.dumps(result)
    return response

# pass through method for submodel POST request
def pass_post_to_hms(request, submodel):
    print("pass_post_to_hms request passed")
    #url = 'http://134.67.114.8/HMSWS/api/WS' + submodel
    url = 'http://localhost:50052/api/WS' + submodel
    print('POST URL: ' + url)
    if request.method == 'POST':
        result = requests.post(url, body=request.body, timeout=1000)
        response = HttpResponse()
        HttpResponse.content = json.dumps(result)
        return response
    else:
        print("GET request with POST arguments. Will implement method to convert POST request to GET request.")
        return Http404

# pass through method for submodel GET request, with query string parameters
def pass_get_to_hms(request, submodel, parameters):
    print("pass_get_to_hms request passed")
    #url = 'http://134.67.114.8/HMSWS/api/WS' + submodel + '/' + parameters
    url = 'http://localhost:50052/api/WS' + submodel + '/' + parameters
    print('GET URL: ' + url)
    if request.method == 'GET':
        result = requests.get(url)
        response = HttpResponse()
        HttpResponse.content = json.dumps(result)
        return response
    else:
        print("POST request with GET arguments. Will implement method to convert GET request to POST request.")
        return Http404


def pass_precip_compare_to_hms(request):
    print("pass_precip_compare_to_hms request passed")
    #url = 'http://134.67.114.8/HMSWS/api/WSPrecipitation'
    url = 'http://localhost:50052/api/WSPrecipitation'
    if request.method == 'POST':
        result = requests.post(url, body=request.body, timeout=1000)
        response = HttpResponse()
        HttpResponse.content = json.dumps(result)
        return response
    else:
        print("GET request with POST arguments. Will implement method to convert POST request to GET request.")
        return Http404

