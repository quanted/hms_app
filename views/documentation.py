from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
import os
import importlib
import hms_app.views.links_left as links_left
import hms_app.models.Documents.views as docs
from . import default_pages


def docs_page(request):
    """
    Base function that constructs the HttpResponse page.
    :param request: Request object
    :param submodel:
    :param header: Default set to none
    :return: HttpResponse object.
    """
    model = 'documentation'
    title = docs.header
    description = docs.description
    submodel = request.path.split("/")[2]
    html = default_pages.build_model_page(request, model, submodel, title, None, description)
    response = HttpResponse()
    response.write(html)
    return response

