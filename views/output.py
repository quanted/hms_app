'''
HMS Hydrology output page functions
'''

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
import importlib, requests, json
import links_left
import os

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
    model_parameters_location = 'hms_app.models.' + model + '.' + model + '_parameters'
    parametersmodule = importlib.import_module(model_parameters_location)
    input_form = getattr(parametersmodule, submodel.title() + 'FormInput')
    form = input_form(request.POST, request.FILES)
    if(form.is_valid()):
        parameters = form.cleaned_data
        parameters['dataset'] = submodel
        if "geojson_file" in request.FILES:
            parameters = spatial_parameter_check(parameters, request.FILES["geojson_file"])
        else:
            parameters = spatial_parameter_check(parameters, None)
        data = get_data(parameters)
        html = create_output_page(model, submodel, data)
    else:
        html = hydrology_input_page_errors(request, model, submodel, header, form=form)
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
        html = create_output_page(model, model, data)
    else:
        html = precip_compare_input_page_errors(request, model, header, form=form)
    response = HttpResponse()
    response.write(html)
    return response


@require_POST
def runoff_compare_output_page(request, model='runoff_compare', header=''):
    """
    Runoff compare output page function.
    :param request: Request object
    :param model: set to 'runoff_compare'
    :param header: default header
    :return: HttpResponse object
    """
    model_parameters_location = 'hms_app.models.' + model + '.' + model + '_parameters'
    parametersmodule = importlib.import_module(model_parameters_location)
    input_form = getattr(parametersmodule, 'RunoffCompareFormInput')
    form = input_form(request.POST)
    if(form.is_valid()):
        parameters = form.cleaned_data
        parameters['source'] = 'compare'
        data = get_runoff_compare_data(parameters)
        html = create_output_page(model, model, data)
    else:
        html = runoff_compare_input_page_errors(request, model, header, form=form)
    response = HttpResponse()
    response.write(html)
    return response


def get_data(parameters):
    """
    Performs the POST call to the HMS backend server for data retrieval.
    :param parameters: Dictionary containing the parameters.
    :return: object constructed from json.loads()
    """                                                             # True will save the current request as a sample.
    # url = 'http://134.67.114.8/HMSWS/api/WSHMS/'                                # server 8 HMS, external
    # url = 'http://172.20.10.18/HMSWS/api/WSHMS/'                              # server 8 HMS, internal
    url = 'http://localhost:50052/api/WSHMS/'                                  # local VS HMS
    # url = 'http://localhost:7777/rest/hms/'                                   # local flask
    # url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/api/WSHMS/'     # HMS backend server variable
    try:
        result = requests.post(str(url), data=parameters, timeout=1000)
    except requests.exceptions.RequestException as e:
        data = json.loads(ERROR_OUTPUT)
        data['metadata']['errorMsg'] = "ERROR: " + str(e.message)
        return data
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
    # url = 'http://134.67.114.8/HMSWS/api/WSPrecipitation/'                              # server 8 HMS, external
    # url = 'http://172.20.10.18/HMSWS/api/WSPrecipitation/'                            # server 8 HMS, internal
    # url = 'http://localhost:50052/api/WSPrecipitation/'                               # local VS HMS
    # url = 'http://localhost:7777/hms/rest/Precipitation/'                             # local flask
    url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/api/WSPrecipitation/'   # HMS backend server variable
    try:
        result = requests.post(str(url), data=parameters, timeout=1000)
    except requests.exceptions.RequestException as e:
        data = json.loads(ERROR_OUTPUT)
        data['metadata']['errorMsg'] = "ERROR: " + str(e.message)
        return data
    data = json.loads(result.content)
    if "Message" in data:
        print("error getting precip compare data")
        data = json.loads(ERROR_OUTPUT)
    return data


def get_runoff_compare_data(parameters):
    """
    Performs the POST call to the HMS backend server for retrieving runoff comparision data.
    :param parameters: Dictionary containing the parameters.
    :return: object constructed from json.loads()
    """
    # url = 'http://134.67.114.8/HMSWS/api/WSLandSurfaceFlow/'                                  # server 8 HMS, external
    # url = 'http://172.20.10.18/HMSWS/api/WSLandSurfaceFlow/'                                  # server 8 HMS, internal
    # url = 'http://localhost:50052/api/WSLandSurfaceFlow/'                                       # local VS HMS
    # url = 'http://localhost:7777/hms/rest/LandSurfaceFlow/'                                   # local flask
    url = str(os.environ.get('HMS_BACKEND_SERVER')) + '/HMSWS/api/WSLandSurfaceFlow/'         # HMS backend server variable
    try:
        result = requests.post(str(url), data=parameters, timeout=1000)
    except requests.exceptions.RequestException as e:
        data = json.loads(ERROR_OUTPUT)
        data['metadata']['errorMsg'] = "ERROR: " + str(e.message)
        return data
    data = json.loads(result.content)
    if "Message" in data:
        print("error getting runoff compare data")
        data = json.loads(ERROR_OUTPUT)
    return data


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
    try:
        columns = {}
        ncolumns = 0
        if("errorMsg" not in data["metadata"]):
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
        return redirect('/hms/' + model + '/' + submodel + '/')
    # Generates html for links left
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, submodel)

    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html


def spatial_parameter_check(parameters, uploadedFile):
    """
    Checks the parameters dictionary for all spatial parameters that are empty and removes them from the parameters list.
    :param parameters: django form inputs
    :return: dictionary of parameters
    """
    p = parameters
    if uploadedFile is not None:
        if p["geojson_file"] is not None:
            p["geojson"] = uploadedFile.read()
            p["geojson_file"] = None

    for key, value in p.items():
        if value is None or value is u'':
            del p[key]
    return p


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


def precip_compare_input_page_errors(request, model='', header='', form=''):
    """
    Constructs html for precip compare page, with input errors.
    :param request: current request object
    :param model: current model
    :param header: current header
    :return: string formatted as html
    """
    import hms_app.models.precip_compare.views as precip_compare_view
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})
    description = precip_compare_view.description
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header,
        'TEXT_PARAGRAPH': description
    })
    html += render_to_string('07ubertext_end_drupal.html', {})
    # -------------------- Form with Errors ---------------- #
    import hms_app.models.precip_compare.precip_compare_inputs as pc_inputs
    html += pc_inputs.precip_compare_input_page(request, model, header, form)
    # ----------------------- end of Form ------------------ #
    html += links_left.ordered_list(model, "")
    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html


def runoff_compare_input_page_errors(request, model='', header='', form=''):
    """
    Constructs html for runoff compare page
    :param request: current request object
    :param model: current model
    :param header: current header
    :return: string formatted as html
    """
    import hms_app.models.runoff_compare.views as runoff_compare_view
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})
    description = runoff_compare_view.description
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header,
        'TEXT_PARAGRAPH': description
    })
    html += render_to_string('07ubertext_end_drupal.html', {})
    # -------------------- Form with Errors ---------------- #
    import hms_app.models.runoff_compare.runoff_compare_inputs as rc_inputs
    html += rc_inputs.runoff_compare_input_page(request, model, header, form)
    # ----------------------- end of Form ------------------ #
    html += links_left.ordered_list(model, "")
    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html

