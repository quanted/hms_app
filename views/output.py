'''
HMS output
'''

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpRequest
import importlib, requests, json
import urllib
import links_left
import os


@require_POST
def hydrology_output_page(request, model='hydrology', submodel='', header=''):
    model_views_location = 'hms_app.models.' + model + '.views'
    viewmodule = importlib.import_module(model_views_location)
    header = viewmodule.header
    model_parameters_location = 'hms_app.models.' + model + '.' + model + '_parameters'
    model_input_location = 'hms_app.models.' + model + '.' + model + '_input'
    parametersmodule = importlib.import_module(model_parameters_location)
    input_form = getattr(parametersmodule, submodel.title() + 'FormInput')
    form = input_form(request.POST)
    if( form.is_valid() ):
        parameters = set_parameters(form.cleaned_data)
        parameters['dataset'] = submodel
        data = get_data(parameters)
        #data = get_sample_data(parameters)          # gets test data
        html = create_output_page(model, submodel, data)
    else:
        html = "Error processing input form."
    response = HttpResponse()
    response.write(html)
    return response


def set_parameters(orderedDict):
    params = {}
    for name in orderedDict:
        params[name] = str(orderedDict[name])
    return params


def get_data(parameters):
    url = 'http://localhost:50052/api/WSHMS/'   #LOCAL HOST PORT WOULD NEED TO BE CHANGED BASED UPON LOCAL SERVER SETUP
    result = requests.post(url, data=parameters, timeout=100)
    data = json.loads(result.content)
    #with open('hms_app/models/hydrology/sample_data.json', 'w') as jsonfile:
    #    json.dump(data, jsonfile)
    return data


def get_sample_data(parameters):
    with open('hms_app/models/hydrology/sample_data.json', 'r') as jsonfile:
        return json.load(jsonfile)



def create_output_page(model, submodel, data):

    #json_data = json_to_array(data['data'])
    json_data = data
    html = render_to_string('01hms_output_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    html += render_to_string('04hms_output_table.html', {
        'TITLE': "HMS " + submodel.title() + " Data",
        'METADATA': json_data["metadata"],
        'DATA': json_data["data"],
        'COLUMN1': 'Data/Time',
        'COLUMN2': 'Data'
    })

    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, submodel)

    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html


def json_to_array(jsondata):
    newList = []
    for key, value in sorted(jsondata.iteritems()):
        temp = [str(key), str(value[0])]
        newList.append(temp)
    return newList

