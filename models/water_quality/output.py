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

# Generic ERROR json data string
ERROR_OUTPUT = '{"dataset": "", "source": "", ' \
               '"metadata": {"errorMsg":"Error retrieving data. Unable to return data from server."},' \
               '"data": {"":[""]}}'

photolysis_default = {
    "input": {
        "contaminant name": "Methoxyclor",
        "contaminant type": "Chemical",
        "water type name": "Pure Water",
        "min wavelength": 297.5,
        "max wavelength": 330,
        "longitude": "83.2",
        "latitude(s)": [
            40,
            -99,
            -99,
            -99,
            -99,
            -99,
            -99,
            -99,
            -99,
            -99
        ],
        "season(s)": [
            "Spring",
            "  ",
            "  ",
            "  "
        ],
        "atmospheric ozone layer": 0.3,
        "initial depth (cm)": "0.001",
        "final depth (cm)": "5",
        "depth increment (cm)": "10",
        "quantum yield": "0.32",
        "refractive index": "1.34",
        "elevation": "0",
        "wavelength table": {
            "297.50": {
                "water attenuation coefficients (m**-1)": "0.069000",
                "chemical absorption coefficients (L/(mole cm))": "11.100000"
            },
            "300.00": {
                "water attenuation coefficients (m**-1)": "0.061000",
                "chemical absorption coefficients (L/(mole cm))": "4.6700000"
            },
            "302.50": {
                "water attenuation coefficients (m**-1)": "0.057000",
                "chemical absorption coefficients (L/(mole cm))": "1.900000"
            },
            "305.00": {
                "water attenuation coefficients (m**-1)": "0.053000",
                "chemical absorption coefficients (L/(mole cm))": "1.100000"
            },
            "307.50": {
                "water attenuation coefficients (m**-1)": "0.049000",
                "chemical absorption coefficients (L/(mole cm))": "0.800000"
            },
            "310.00": {
                "water attenuation coefficients (m**-1)": "0.045000",
                "chemical absorption coefficients (L/(mole cm))": "0.5300000"
            },
            "312.50": {
                "water attenuation coefficients (m**-1)": "0.043000",
                "chemical absorption coefficients (L/(mole cm))": "0.330000"
            },
            "315.00": {
                "water attenuation coefficients (m**-1)": "0.041000",
                "chemical absorption coefficients (L/(mole cm))": "0.270000"
            },
            "317.50": {
                "water attenuation coefficients (m**-1)": "0.039000",
                "chemical absorption coefficients (L/(mole cm))": "0.1600000"
            },
            "320.00": {
                "water attenuation coefficients (m**-1)": "0.037000",
                "chemical absorption coefficients (L/(mole cm))": "0.100000"
            },
            "323.10": {
                "water attenuation coefficients (m**-1)": "0.035000",
                "chemical absorption coefficients (L/(mole cm))": "0.060000"
            },
            "330.00": {
                "water attenuation coefficients (m**-1)": "0.029000",
                "chemical absorption coefficients (L/(mole cm))": "0.020000"
            }
        }
    }
}


@require_POST
def water_quality_output(request, model='water_quality', submodel='', header=''):
    parameters = json.dumps({"input": construct_dictionary(submodel, request.POST.dict())})
    data = get_data(submodel, parameters)
    html = create_output_page(model, submodel, data, parameters)
    response = HttpResponse()
    response.write(html)
    return response


@require_POST
def water_quality_json_output(request, model='water_quality', submodel='', header=''):
    parameters = request.POST["json_input"]
    data = get_data(submodel, parameters)
    html = create_output_page(model, submodel, data, parameters)
    response = HttpResponse()
    response.write(html)
    return response


def construct_dictionary(submodule, parameters):
    valid_parameters = {}
    if submodule == "photolysis":
        for key, value in parameters.items():
            if key == 'wavelength_table':
                tbl = json.loads(value)
                wl_input = {}
                for i in range(1, len(tbl)):
                    wl_row = {tbl[0][1]: tbl[i][1], tbl[0][2]: tbl[i][2]}
                    wl_input[tbl[i][0]] = wl_row
                valid_parameters[key.replace('_', ' ')] = wl_input
            elif value is "":
                if key.replace('_', ' ') in photolysis_default["input"].keys():
                    valid_parameters[key.replace('_', ' ')] = photolysis_default["input"][key.replace('_', ' ')]
            else:
                if parameters['typical_ephemeride_values'] == "no":
                    if "solar_declination" in key or "right_ascension" in key or "sidereal_time" in key:
                        k = key.split('_')
                        full_key = k[0] + " " + k[1]
                        if full_key in valid_parameters.keys():
                            valid_parameters[full_key].append(value)
                        else:
                            valid_parameters[full_key] = [value]
                    else:
                        valid_parameters[key.replace('_', ' ')] = value
                else:
                    valid_parameters[key.replace('_', ' ')] = value
    return valid_parameters


def get_data(model, parameters):
    """
    Performs the POST call to the HMS backend server for retrieving comparision data.
    :param model: comparision model to compare
    :param parameters: Dictionary containing the parameters.
    :return: object constructed from json.loads()
    """
    url = ""
    if model == "photolysis":
        # url = 'http://134.67.114.8/HMSWS/api/WSSolar/run'                                 # server 8 HMS, external
        # url = 'http://172.20.10.18/HMSWS/api/WSPrecipitation/'                            # server 8 HMS, internal
        # url = 'http://localhost:60049/api/WSSolar/run'  # local VS HMS
        # url = 'http://localhost:7777/hms/rest/Precipitation/'                             # local flask
        url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/api/WSSolar/run'        # HMS backend server variable
    try:
        result = requests.post(str(url), json=json.loads(parameters), timeout=10000)
    except requests.exceptions.RequestException as e:
        data = json.loads(ERROR_OUTPUT)
        data['metadata']['errorMsg'] = "ERROR: " + str(e)
        return data
    data = json.loads(result.content)
    if "Message" in data:
        print("error getting precip compare data")
        data = json.loads(ERROR_OUTPUT)
    return data


def create_output_page(model, submodel, data, input):
    """
    Generates the html for the output page.
    :param model: model of the data
    :param submodel: submodel of the data
    :param data: json object of the data
    :param dataset: dataset name, may be the same as submodel
    :param location: geographic location of request, used for labeling
    :return: string structured as html.
    """
    html = render_to_string('01hms_output_basic_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model,
        'LABEL': submodel
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    # HMS water quality imports html
    html += render_to_string('03hms_waterquality_imports.html', {})

    # Generates html for metadata and data tables.
    """
     Columns setup and ordering logic. Keys are checked for numerical value, which is used as the new key for the dict.
    """
    try:
        dt_day_table = data["dtDay"]
        dt_kl_table = data["dtKL"]
        # -------------------------- #

        html += render_to_string('04hms_waterquality_output.html', {
            'MODEL': model,
            'SUBMODEL': submodel.title(),
            'TITLE': "HMS " + submodel.replace('_', ' ').title() + " Data",
            'INPUT_DATA': input,
            'DAYTABLE': dt_day_table,
            'KLTABLE': dt_kl_table
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
