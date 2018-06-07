'''
HMS Meteorology output page functions
'''

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.shortcuts import redirect
import importlib
import requests
import json
import hms_app.views.links_left as links_left
import os
import time  ###

# TESTING
from ..swag_request import SwagRequest as swag

# Generic ERROR json data string
ERROR_OUTPUT = '{"dataset": "", "source": "", ' \
               '"metadata": {"errorMsg":"Error retrieving data. Unable to return data from server."},' \
               '"data": {"":[""]}}'


@require_POST
def meteorology_output_page(request, model='meteorology', submodel='', header=''):
    """
	Default meteorology output page function, constructs complete output page
	:param request: Request object
	:param model: set to 'hydrology'
	:param submodel: string of the specific submodel that made the call to the output page
	:param header: default header
	:return: HttpResponse object
	"""
    model_parameters_location = 'hms_app.models.' + model + '.' + model + '_parameters'
    parametersmodule = importlib.import_module(model_parameters_location)
    input_form = getattr(parametersmodule, submodel.title() + 'FormInput')
    form = input_form(request.POST, request.FILES)
    if form.is_valid():
        parameters = form.cleaned_data
        if parameters["model"] == "year":
            request_parameters = {
                "model": str(parameters['model']).lower(),
                "localTime": str(parameters['local_time']),
                "dateTimeSpan": {
                    "startDate": str(parameters['year'] + "-01-01"),
                },
                "geometry": {
                    "point": {
                        "latitude": str(parameters['latitude']),
                        "longitude": str(parameters['longitude'])
                    },
                    "timezone": {
                        "offset": str(parameters['timezone'])
                    }
                }
            }
        else:
            request_parameters = {
                "model": str(parameters['model']).lower(),
                "dateTimeSpan": {
                    "startDate": str(parameters['date']),
                },
                "geometry": {
                    "point": {
                        "latitude": str(parameters['latitude']),
                        "longitude": str(parameters['longitude'])
                    },
                    "timezone": {
                        "offset": str(parameters['timezone'])
                    }
                }
            }
        data = get_data(model, "solar", request_parameters)
        location = str(parameters['latitude']) + ", " + str(parameters['longitude'])
        html = create_meteorology_output_page(model, submodel, data, submodel.capitalize(), location)
    else:
        html = hydrology_input_page_errors(request, model, submodel, header, form=form)
    response = HttpResponse()
    response.write(html)
    return response



def set_geometry_metadata(form_data):
    if form_data == '':
        return {}
    lines = form_data.split(',')
    g_meta = {}
    for line in lines:
        key_value = line.split(':')
        g_meta[key_value[0]] = key_value[1]
    return g_meta

def get_data(model, submodel, parameters):
    """
	Performs the POST call to the HMS backend server for data retrieval.
	:param submodel: submodel of requested data
	:param parameters: Dictionary containing the parameters.
	:return: object constructed from json.loads()
	"""
    if os.environ['HMS_LOCAL'] == "True":
        # url = 'http://134.67.114.8/HMSWS/api/' + submodel                                  # server 8 HMS, external
        # url = 'http://172.20.10.18/HMSWS/api/WSHMS/'                                  # server 8 HMS, internal
        url = 'http://localhost:60049/api/' + model + '/' + submodel  # local VS HMS
    # url = 'http://localhost:7777/rest/hms/'                                       # local flask
    else:
        url = str(os.environ.get(
            'HMS_BACKEND_SERVER')) + '/HMSWS/api/' + model + '/' + submodel  # HMS backend server variable
    print("url: " + url)
    try:
        result = requests.post(str(url), json=parameters, timeout=10000)
    except requests.exceptions.RequestException as e:
        data = json.loads(ERROR_OUTPUT)
        data['metadata']['errorMsg'] = "ERROR: " + str(e)
        return data
    data = json.loads(result.content)
    if "Message" in data:
        data = json.loads(ERROR_OUTPUT)
    return data



def create_meteorology_output_page(model, submodel, data, dataset, location):
    """
	Generates the html for the meteorology output page.
	:param model: model of the data
	:param submodel: submodel of the data
	:param data: json object of the data
	:param dataset: dataset name, may be the same as submodel
	:param location: geographic location of request, used for labeling
	:return: string structured as html.
	"""
    label = dataset + ": " + location
    html = render_to_string('01hms_output_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model,
        'LABEL': label
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    html += render_to_string('04hms_met_output.html', {
        'MODEL': model,
        'SUBMODEL': submodel,
        'TITLE': "HMS " + model.replace('_', ' ').title(),
        'COLUMN_HEADERS': str(data['metadata']['columns']).split(", "),
        'DATA_ROWS': data['data'],
        'DATA': data,
        'METADATA': data['metadata'],
        'DATASET': dataset,
        'LABEL': label
    })

    # Generates html for links left
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, submodel)

    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    html += render_to_string('04hms_met_output_imports.html', {})
    return html

def hydrology_input_page_errors(request, model='', submodel='', header='', form=''):
    """
	Constructs the html for the hydrology input pages, containing errors in the form.
	:param request: current request object
	:param model: current model
	:param submodel: current submodel
	:param header: current header
	:param form: Previous form data.
	:return: returns a string formatted as html
	"""
    import hms_app.views.hydrology_submodels as hydro_sub
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    description = hydro_sub.get_submodel_description(submodel)
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header,
        'TEXT_PARAGRAPH': description
    })
    html += render_to_string('07ubertext_end_drupal.html', {})
    # --------------- Form with Errors --------------- #
    import hms_app.models.hydrology.hydrology_inputs as hydro_form
    html += hydro_form.hydrology_input_page(request, model, submodel, header, form)
    # ------------------ end of Form ----------------- #
    html += links_left.ordered_list(model, submodel)
    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html