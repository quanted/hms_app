from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import json


""" REST endpoints for HMS django frontend
"""
"""
"""

@require_GET
def delineate_watershed(request):
    request_query = request.GET.dict()
    latitude = request_query["latitude"]
    longitude = request_query["longitude"]
    # TODO: Complete function