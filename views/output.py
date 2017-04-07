'''
HMS hydrology output page functions
'''

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.shortcuts import redirect
import importlib, requests, json, time
import links_left
import os


# Default hydrology output page function, constructs complete output page
@require_POST
def hydrology_output_page(request, model='hydrology', submodel='', header=''):
    model_views_location = 'hms_app.models.' + model + '.views'
    # viewmodule = importlib.import_module(model_views_location)
    # header = viewmodule.header
    model_parameters_location = 'hms_app.models.' + model + '.' + model + '_parameters'
    # model_input_location = 'hms_app.models.' + model + '.' + model + '_input'
    parametersmodule = importlib.import_module(model_parameters_location)
    input_form = getattr(parametersmodule, submodel.title() + 'FormInput')
    form = input_form(request.POST)
    if( form.is_valid() ):
        parameters = set_parameters(form.cleaned_data)
        parameters['dataset'] = submodel
        data = get_data(parameters)
        #data = get_sample_data(parameters)          # gets sample test data
        html = create_output_page(model, submodel, data)
    else:
        print("INPUT ERROR: Please provided required inputs.")
        return redirect('/hms/' + model + '/' + submodel)
    response = HttpResponse()
    response.write(html)
    return response


@require_POST
def precip_compare_output_page(request, model='precip_compare', header=''):
    model_parameters_location = 'hms_app.models.' + model + '.' + model + '_parameters'
    parametersmodule = importlib.import_module(model_parameters_location)
    input_form = getattr(parametersmodule, 'PrecipitationCompareFormInput')
    form = input_form(request.POST)
    if( form.is_valid() ):
        parameters = set_parameters(form.cleaned_data)
        parameters['source'] = 'compare'            # Required to select the comparision method on the HMS backend
        data = get_precip_compare_data(parameters)
        #data = get_precip_compare_sample_data(parameters)
        html = create_output_page(model, "", data)
    else:
        print("INPUT ERROR: Invalid inputs found.")
        return redirect('/hms/precip_compare/')
    response = HttpResponse()
    response.write(html)
    return response


# Collects parameters from the input form
def set_parameters(orderedDict):
    params = {}
    for name in orderedDict:
        params[name] = str(orderedDict[name])
    return params


# Makes call to HMS server for data retrieval
def get_data(parameters):
    sample = False                              # Set to save data as sample
    url = 'http://134.67.114.8/HMSWS/api/WSHMS/'   #TODO: LOCAL HOST PORT WOULD NEED TO BE CHANGED BASED UPON LOCAL SERVER SETUP
    # url = 'http://localhost:50052/api/WSHMS/'
    result = requests.post(url, data=parameters, timeout=360)
    if sample == True:
        with open('hms_app/models/hydrology/sample_data.json', 'w') as jsonfile:
            json.dumps(result.content, jsonfile)
    data = json.loads(result.content)
    return data


# Makes call to HMS server for precip comparision data
def get_precip_compare_data(parameters):
    sample = False                                         # Set to save data as sample
    #url = 'http://134.67.114.8/HMSWS/api/WSPrecipitation/'
    url = 'http://localhost:50052/api/WSPrecipitation/'     #TODO: LOCAL HOST PORT WOULD NEED TO BE CHANGED BASED UPON LOCAL SERVER SETUP
    result = requests.post(url, data=parameters, timeout=1000)
    if sample == True:
        with open('hms_app/models/precip_compare/sample_data.json', 'w') as jsonfile:
            json.dump(result.content, jsonfile)
    data = json.loads(result.content)
    return data


# Returns sample data from file
def get_sample_data(parameters):
    with open('hms_app/models/hydrology/sample_data.json', 'r') as jsonfile:
        return json.load(jsonfile)

    # Returns sample data from file
def get_precip_compare_sample_data(parameters):
    with open('hms_app/models/precip_compare/sample_data.json', 'r') as jsonfile:
        return json.load(jsonfile)


# Creates html for output page
def create_output_page(model, submodel, data):

    json_data = json.dumps(data)
    # Unique hms output html necessary due to additional js requirements on page.

    html = render_to_string('01hms_output_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})
    # Generates html for metadata and data tables.
    if model == "precip_compare":
        html += render_to_string('04hms_output_table.html', {
            'ALLDATA': json_data,
            'MODEL': model,
            'SUBMODEL': model,
            'TITLE': "HMS " + model.replace('_', ' ').title() + " Data",
            'METADATA': data["metadata"],
            'DATA': data["data"],
            'COLUMN1': data["metadata"]["column_1"],
            'COLUMN2': data["metadata"]["column_2"],
            'COLUMN3': data["metadata"]["column_3"],
            'COLUMN4': data["metadata"]["column_4"],
            'COLUMN5': data["metadata"]["column_5"]
        })
    else:
        print 'model: ' + model
        print 'submodel: ' + submodel
        html += render_to_string('04hms_output_table.html', {
            'MODEL': model,
            'SUBMODEL': submodel,
            'TITLE': "HMS " + submodel.replace('_', ' ').title() + " Daily Data",
            'ALLDATA': json_data,
            'METADATA': data["metadata"],
            'DATA': data["data"],
            'COLUMN1': 'Date/Time',
            'COLUMN2': 'Data'
        })
    # Generates html for links left
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, submodel)

    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html

