'''
HMS Hydrology output page functions
'''

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
import importlib, requests, json
import links_left
import os, collections

# Generic ERROR json data string
ERROR_OUTPUT = '{"dataset": null, "source": null, ' \
               '"metadata": {"errorMsg":"Error retrieving data. Unable to return data from server."},' \
               '"data": null}'


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
    model_parameters_location = 'hms_app.models.' + model + '.' + model + '_parameters'
    parametersmodule = importlib.import_module(model_parameters_location)
    input_form = getattr(parametersmodule, submodel.title() + 'FormInput')
    form = input_form(request.POST)
    if(form.is_valid()):
        parameters = form.cleaned_data
        parameters['dataset'] = submodel
        parameters = spatial_parameter_check(parameters)
        data = get_data(parameters)
        # data = get_sample_data(parameters)                        # gets sample test data
        html = create_output_page(model, submodel, data)
    else:
        # TODO: Add descriptive error handling of form validation. Currently reloads input page.
        print("INPUT FORM ERROR: Please provide required inputs.")
        # errors = form.errors
        return redirect('/hms/' + model + '/' + submodel + '/')
    response = HttpResponse()
    response.write(html)
    return response


@require_POST
def precip_compare_output_page(request, model='precip_compare', header=''):
    """
    Precipitation compare output page function.
    :param request: Request object
    :param model: set to 'precip_compare'
    :param header: default header
    :return: HttpResponse object
    """
    model_parameters_location = 'hms_app.models.' + model + '.' + model + '_parameters'
    parametersmodule = importlib.import_module(model_parameters_location)
    input_form = getattr(parametersmodule, 'PrecipitationCompareFormInput')
    form = input_form(request.POST)
    if(form.is_valid()):
        parameters = form.cleaned_data
        parameters['source'] = 'compare'
        data = get_precip_compare_data(parameters)
        #data = get_precip_compare_sample_data(parameters)
        html = create_output_page(model, model, data)
    else:
        # TODO: Add descriptive error handling of form validation. Currently reloads input page.
        print("INPUT FORM ERROR: Invalid inputs found.")
        return redirect('/hms/precip_compare/')
    response = HttpResponse()
    response.write(html)
    return response


def get_data(parameters):
    """
    Performs the POST call to the HMS backend server for data retrieval.
    :param parameters: Dictionary containing the parameters.
    :return: object constructed from json.loads()
    """
    sample = False                                                              # True will save the current request as a sample.
    # url = 'http://134.67.114.8/HMSWS/api/WSHMS/'                                # server 8 HMS, external
    # url = 'http://172.20.10.18/HMSWS/api/WSHMS/'                              # server 8 HMS, internal
    url = 'http://localhost:50052/api/WSHMS'                                  # local VS HMS
    # url = 'http://localhost:7777/rest/hms/'                                   # local flask
    # url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/api/WSHMS/'     # HMS backend server variable
    result = requests.post(str(url), data=parameters, timeout=1000)
    if sample == True:
        with open('hms_app/models/hydrology/sample_data.json', 'w') as jsonfile:
            json.dumps(result.content, jsonfile)
    data = json.loads(result.content)
    if "Message" in data:
        data = json.loads(ERROR_OUTPUT)
    return data


def get_precip_compare_data(parameters):
    """
    Performs the POST call to the HMS backend server for retrieving precip comparision data.
    :param parameters: Dictionary containing the parameters.
    :return: object constructed from json.loads()
    """
    sample = False                                                                      # True will save the current request as a sample.
    # url = 'http://134.67.114.8/HMSWS/api/WSPrecipitation/'                              # server 8 HMS, external
    # url = 'http://172.20.10.18/HMSWS/api/WSPrecipitation/'                            # server 8 HMS, internal
    url = 'http://localhost:50052/api/WSPrecipitation/'                               # local VS HMS
    # url = 'http://localhost:7777/rest/hms/Precipitation/'                             # local flask
    # url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/api/WSPrecipitation/'   # HMS backend server variable
    result = requests.post(str(url), data=parameters, timeout=1000)
    if sample == True:
        with open('hms_app/models/precip_compare/sample_data.json', 'w') as jsonfile:
            json.dump(result.content, jsonfile)
    data = json.loads(result.content)
    if "Message" in data:
        print("error getting precip compare data")
        data = json.loads(ERROR_OUTPUT)
    return data


def get_sample_data(parameters):
    """
    Gets locally stored sample data for testing.
    :param parameters: Not used.
    :return: object constructed from json.load()
    """
    with open('hms_app/models/hydrology/sample_data.json', 'r') as jsonfile:
        return json.load(jsonfile)

    # Returns sample data from file
def get_precip_compare_sample_data(parameters):
    """
    Gets locally stored sample data for testing.
    :param parameters: Not used.
    :return: object constructed from json.load()
    """
    with open('hms_app/models/precip_compare/sample_data.json', 'r') as jsonfile:
        return json.load(jsonfile)


def create_output_page(model, submodel, data):
    """
    Generates the html for the output page.
    :param model: model of the data
    :param submodel: submodel of the data
    :param data: json object of the data
    :return: string structured as html.
    """
    # json_data = json.dumps(data)
    html = render_to_string('01hms_output_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    # Generates html for metadata and data tables.
    """
     Columns setup and ordering logic. Keys are checked for numerical value, which is used as the new key for the dict.
    """
    columns = {}
    ncolumns = len(data["data"][data["data"].keys()[0]])
    for key in data["metadata"]:
        if "column_" in key:
            columns[key] = data["metadata"][key]
    if len(columns) < ncolumns:
        for key in data["metadata"]:
            if "timeseries_" in key:
                k = key.split('_')
                columns[str(k[len(k)-1])] = data["metadata"][key]
    if "date/time" not in columns.keys() and "Date/Time" not in columns.keys() and len(columns)-1 != ncolumns:
        columns["0"] = "Date/Time"
    if len(columns) == 1:
        columns["1"] = "Data"
    columns = [value for (key, value) in sorted(columns.items())]           # Sorts values by key.
    # -----------------------------------------------------------
    try:
        html += render_to_string('04hms_output_table_2.html',{
            'MODEL': model,
            'SUBMODEL': submodel,
            'TITLE': "HMS " + model.replace('_', ' ').title() + " Data",
            'METADATA': data["metadata"],
            'DATA': data["data"],
            'COLUMNS': columns
        })
    except:
        print("ERROR: Unable to construct output tables.")
        #TODO: Do something here...

    # ------------ OBSOLUTE Manual column setup ----------- #
    # if model == "precip_compare":
    #     try:
    #         html += render_to_string('04hms_output_table.html', {
    #           #'ALLDATA': json_data,
    #             'MODEL': model,
    #             'SUBMODEL': model,
    #             'TITLE': "HMS " + model.replace('_', ' ').title() + " Data",
    #             'METADATA': data["metadata"],
    #             'DATA': data["data"],
    #             'COLUMN1': data["metadata"]["column_1"],
    #             'COLUMN2': data["metadata"]["column_2"],
    #             'COLUMN3': data["metadata"]["column_3"],
    #             'COLUMN4': data["metadata"]["column_4"],
    #             'COLUMN5': data["metadata"]["column_5"]
    #         })
    #     except:
    #         html += render_to_string('04hms_output_table.html', {
    #             'MODEL': model,
    #             'SUBMODEL': submodel,
    #             'TITLE': "HMS " + submodel.replace('_', ' ').title() + " Daily Data",
    #             #'ALLDATA': json_data,
    #             'METADATA': data["metadata"],
    #             'DATA': data["data"],
    #             'COLUMN1': 'Date/Time',
    #             'COLUMN2': 'Data'
    #         })
    # else:
    #     html += render_to_string('04hms_output_table.html', {
    #         'MODEL': model,
    #         'SUBMODEL': submodel,
    #         'TITLE': "HMS " + submodel.replace('_', ' ').title() + " Daily Data",
    #         #'ALLDATA': json_data,
    #         'METADATA': data["metadata"],
    #         'DATA': data["data"],
    #         'COLUMN1': 'Date/Time',
    #         'COLUMN2': 'Data'
    #     })

    # Generates html for links left
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, submodel)

    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html


def spatial_parameter_check(parameters):
    """
    Checks the parameters dictionary for all spatial parameters that are empty and removes them from the parameters list.
    :param parameters: django form inputs
    :return: dictionary of parameters
    """
    p = parameters
    for key, value in p.items():
        if value == None:
            del p[key]
    return p

