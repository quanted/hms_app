from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import os


def webapp_view(request, exception=None):
    """
    Access epa-cyano-web Angular application.
    """
    html = render_to_string('hms_webapp/index.html')
    response = HttpResponse()
    response.write(html)
    return response
