import logging
import json
import requests
from json import JSONDecodeError
from django.http import HttpResponseBadRequest
from urllib.parse import unquote
import bleach

logger = logging.getLogger(__name__)


class SanitizeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def clean_dict(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = self.clean_dict(value)
            else:
                data[key] = bleach.clean(value)
        return data

    def __call__(self, request):
        request.url = unquote(request.get_full_path())
        if request.method == 'POST':
            if request.content_type == 'application/json':
                if len(request.POST) == 0:
                    try:
                        request_body = (request.body.decode("utf-8")).replace('\t', '').replace('\r\n', '')
                        if type(request_body) == str:
                            data = json.loads(request_body)
                        else:
                            data = request_body
                    except JSONDecodeError as e:
                        logger.warn("Unable to load JSON data in POST requests")
                        return HttpResponseBadRequest(content=f"Unable to load JSON data in POST requests".encode("utf-8"))
                else:
                    data = request.POST
            else:
                logger.warn("Only JSON data is supported for POST requests")
                return HttpResponseBadRequest(content=f"Only JSON data is supported for POST requests".encode("utf-8"))
            for key, value in data.items():
                data[key] = bleach.clean(value)
            request.POST = data
        elif request.method == 'GET':
            params = request.GET.copy()
            for key in params:
                params[key] = bleach.clean(params[key])
            request.GET = params

        response = self.get_response(request)
        return response