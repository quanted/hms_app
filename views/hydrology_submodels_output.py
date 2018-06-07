'''
HMS Hydrology output page functions
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
def hydrology_output_page(request, model='hydrology', submodel='', header=''):
    """
	Default hydrology output page function, constructs complete output page
	:param request: Request object
	:param model: set to 'hydrology'
	:param submodel: string of the specific submodel that made the call to the output page
	:param header: default header
	:return: HttpResponse object
	"""
    model_parameters_location = 'hms_app.models.' + 'hydrology' + '.' + 'hydrology' + '_parameters'
    parametersmodule = importlib.import_module(model_parameters_location)
    input_form = getattr(parametersmodule, model.title() + 'FormInput')
    form = input_form(request.POST, request.FILES)
    if form.is_valid():
        parameters = form.cleaned_data
        if (parameters["source"] == "ncdc" and submodel.title() != "Evapotranspiration"):
            request_parameters = {
                "source": str(parameters['source']).lower(),
                "dateTimeSpan": {
                    "startDate": str(parameters['startDate']),
                    "endDate": str(parameters['endDate'])
                },
                "geometry": {
                    "geometryMetadata": set_geometry_metadata(parameters["geometrymetadata"])
                },
                "temporalResolution": str(parameters['temporalresolution']),
                "timeLocalized": str(parameters['timelocalized'])
            }
            request_parameters["geometry"]["geometryMetadata"]["stationID"] = str(parameters["stationID"])
        elif (submodel.title() == "Evapotranspiration"):
            request_parameters = {
                "source": str(parameters['source']).lower(),
                "algorithm": str(parameters['algorithm']).lower(),
                "dateTimeSpan": {
                    "startDate": str(parameters['startDate']),
                    "endDate": str(parameters['endDate'])
                },
                "temporalResolution": str(parameters['temporalresolution']),
                "timeLocalized": str(parameters['timelocalized']),
                "albedo": str(parameters['albedo']),
                "centrallongitude": str(parameters['centlong']),
                "sunangle": str(parameters['sunangle']),
                "emissivity": str(parameters['emissivity']),
                "model": str(parameters['model']),
                "zenith": str(parameters['zenith']),
                "lakesurfacearea": str(parameters['lakesurfarea']),
                "lakedepth": str(parameters['lakedepth']),
                "subsurfaceresistance": str(parameters['subsurfres']),
                "stomatalresistance": str(parameters['stomres']),
                "leafwidth": str(parameters['leafwidth']),
                "roughnesslength": str(parameters['roughlength']),
                "vegetationheight": str(parameters['vegheight'])
            }
            if(parameters["source"] != "ncdc"):
                request_parameters["geometry"] = {
                    "point": {
                        "latitude": str(parameters['latitude']),
                        "longitude": str(parameters['longitude'])
                    },
                    "geometryMetadata": set_geometry_metadata(parameters["geometrymetadata"])
                }
            elif(parameters["source"] == "ncdc"):
                request_parameters["geometry"] = {
                    "geometryMetadata": set_geometry_metadata(parameters["geometrymetadata"])
                }
                request_parameters["geometry"]["geometryMetadata"]["stationID"] = str(parameters["stationID"])
            if (parameters["algorithm"] == "shuttleworthwallace"):
                request_parameters["leafareaindices"] = {
                    1: parameters['leafarea'][0],
                    2: parameters['leafarea'][1],
                    3: parameters['leafarea'][2],
                    4: parameters['leafarea'][3],
                    5: parameters['leafarea'][4],
                    6: parameters['leafarea'][5],
                    7: parameters['leafarea'][6],
                    8: parameters['leafarea'][7],
                    9: parameters['leafarea'][8],
                    10: parameters['leafarea'][9],
                    11: parameters['leafarea'][10],
                    12: parameters['leafarea'][11]
                }
            elif (parameters["algorithm"] == "mcjannett"):
                request_parameters["airtemperature"] = {
                    1: str(parameters['airtemps'][0]),
                    2: str(parameters['airtemps'][1]),
                    3: str(parameters['airtemps'][2]),
                    4: str(parameters['airtemps'][3]),
                    5: str(parameters['airtemps'][4]),
                    6: str(parameters['airtemps'][5]),
                    7: str(parameters['airtemps'][6]),
                    8: str(parameters['airtemps'][7]),
                    9: str(parameters['airtemps'][8]),
                    10: str(parameters['airtemps'][9]),
                    11: str(parameters['airtemps'][10]),
                    12: str(parameters['airtemps'][11])
                }
        else:
            request_parameters = {
                "source": str(parameters['source']).lower(),
                "dateTimeSpan": {
                    "startDate": str(parameters['startDate']),
                    "endDate": str(parameters['endDate'])
                },
                "geometry": {
                    "point": {
                        "latitude": str(parameters['latitude']),
                        "longitude": str(parameters['longitude'])
                    },
                    "geometryMetadata": set_geometry_metadata(parameters["geometrymetadata"])
                },
                "temporalResolution": str(parameters['temporalresolution']),
                "timeLocalized": str(parameters['timelocalized'])
            }
        if "soilmoisture" in submodel:
            request_parameters["layers"] = parameters["layers"]

        # target = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/api/' + submodel
        # swaggernurl = "https://qedinternal.epa.gov/hms/api_doc/swagger"
        # request_parameters = swag(method="POST", target_url=target, parameters=parameters, swagger_url=swaggernurl)
        print(request_parameters)
        data = get_data(model, submodel, request_parameters)
        location = str(parameters['latitude']) + ", " + str(parameters['longitude'])
        html = create_output_page(model, submodel, data, submodel.capitalize(), location)
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


def create_output_page(model, submodel, data, dataset, location):
    """
	Generates the html for the output page.
	:param model: model of the data
	:param submodel: submodel of the data
	:param data: json object of the data
	:param dataset: dataset name, may be the same as submodel
	:param location: geographic location of request, used for labeling
	:return: string structured as html.
	"""
    # json_data = json.dumps(data)
    label = dataset + ": " + location
    html = render_to_string('01hms_output_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model,
        'LABEL': label
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    # Generates html for metadata and data tables.
    """
	 Columns setup and ordering logic. Keys are checked for numerical value, which is used as the new key for the dict.
	"""
    # sources = data["dataSource"].split(', ')

    try:
        columns = {}
        ncolumns = 0
        if "ERROR" not in data["metadata"]:
            ncolumns = len(data["data"][list(data["data"].keys())[0]])
        for key in data["metadata"]:
            if "column_" in key:
                columns[key] = data["metadata"][key]
        if len(columns) < ncolumns:
            for key in data["metadata"]:
                if "timeseries_" in key:
                    k = key.split('_')
                    columns[str(k[len(k) - 1])] = data["metadata"][key]
        if "date/time" not in columns.keys() and "Date/Time" not in columns.keys() and len(columns) - 1 != ncolumns:
            columns["0"] = "Date/Time"
        if len(columns) == 1:
            columns["1"] = "Data"
        columns = [value for (key, value) in sorted(columns.items())]  # Sorts values by key.
        # -------------------------- #
        stats = []
        dcolumns = columns[1:len(columns)]
        for datasets in dcolumns:
            dstats = [datasets,
                      data["metadata"].get(datasets + "_average", ""),
                      data["metadata"].get(datasets + "_sum", ""),
                      data["metadata"].get(datasets + "_standard_deviation", ""),
                      data["metadata"].get(datasets + "_ncdc_R-Squared", ""),
                      data["metadata"].get(datasets + "_ncdc_gore", "")]
            stats.append(dstats)
        html += render_to_string('04hms_output_table_2.html', {
            'MODEL': model,
            'SUBMODEL': submodel,
            'TITLE': "HMS " + model.replace('_', ' ').title() + " Data",
            'METADATA': data["metadata"],
            'DATA': data["data"],
            'COLUMNS': columns,
            'STATS': stats,
            'DATASET': dataset,
            'LABEL': label
        })
    except Exception as ex:
        print("ERROR: Unable to construct output tables.")
        return redirect('/hms/' + model + '/' + submodel + '/')
    # Generates html for links left
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, submodel)

    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
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

