'''
HMS Hydrology output page functions
'''

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import redirect
import importlib
import requests
import json
import hms_app.views.links_left as links_left
import os
import hms_app.models.hydrodynamic.views as hydro_d

# TESTING
from ..swag_request import SwagRequest as swag

# Generic ERROR json data string
ERROR_OUTPUT = '{"dataset": "", "source": "", ' \
               '"metadata": {"errorMsg":"Error retrieving data. Unable to return data from server."},' \
               '"data": {"":[""]}}'



submodel_list = ['constantvolume', 'changingvolume',
                 'kinematicwave']

# @ensure_csrf_cookie
# def submodel_page(request, submodel, header='none'):
#     """
#     Base function that constructs the HttpResponse page.
#     :param request: Request object
#     :param submodel:
#     :param header: Default set to none
#     :return: HttpResponse object.
#     """
#
#     urlpath = request.path.split('/')
#     model = 'hydrodynamic'
#     submodel = urlpath[urlpath.index(model) + 1]
#     #header = get_submodel_header(submodel)
#     #html = build_submodel_page(request, model, submodel, header)
#     response = HttpResponse()
#     response.write(html)
#     return response
#
# def get_submodel_header(submodel):
#     """
#     Gets the submodel page header.
#     :param submodel: Current submodel
#     :return: header as a string
#     """
#     submodelTitle = submodel.replace('_', ' ').title()
#     if (submodelTitle == "constant_volume"):
#         submodelTitle = "Constant Volume"
#     elif (submodelTitle == "changing_volume"):
#         submodelTitle = "Changing Volume"
#     elif (submodelTitle == "kinematic_wave"):
#         submodelTitle = "Kinematic Wave"
#     return hydro_d.header + " - " + submodelTitle



def get_model_input_module(model):
    """
    Gets the object of the model containing the submodule input functions.
    :param model: current model
    :return: object of the model containing the inputs
    """
    model_module_location = 'hms_app.models.' + model + '.' + model + '_inputs'
    model_input_module = importlib.import_module(model_module_location)
    return model_input_module


def hydrodynamics_output_page(request, model='hydrodynamic', submodel='', header=''):

    """
    Default hydrodynamic output page function, constructs complete output page
    :param request: Request object
    :param model: set to 'hydrodynamic'
    :param submodel: string of the specific submodel that made the call to the output page
    :param header: default header
    :return: HttpResponse object
    """
    model_parameters_location = 'hms_app.models.' + 'hydrodynamic' + '.' + model + '_parameters'
    parametersmodule = importlib.import_module(model_parameters_location)
    print(submodel)
    print(submodel.title())
    input_form = getattr(parametersmodule, submodel.title() + 'FormInput')
    form = input_form(request.POST, request.FILES)
    if form.is_valid():
        parameters = form.cleaned_data
        if submodel == "constant_volume":
            request_parameters = {
                "dateTimeSpan": {
                       "startDate": str(parameters['startDate']),
                       "endDate": str(parameters['endDate']),
                "timestep": str(parameters['timestep']),
                "segments": str(parameters['segments']),
                "boundary_flow": str(parameters['boundary_flow']),
                },
            }
        elif submodel == "changing_volume":
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
        elif submodel == "kinematic_wave":
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
        data = get_data(model, submodel, request_parameters)
        #print(data)
        html = create_hydrodynamic_output_page(model, submodel, data, submodel.capitalize()) ##hydrodynamic_
        #print(html)

    else:
        html = hydrodynamic_input_page_errors(request, model, submodel, header, form=form)
    response = HttpResponse()
    response.write(html)
    return response


def get_data(model, submodel, parameters):
    """
    Performs the POST call to the HMS backend server for data retrieval.
    :param submodel: submodel of requested data
    :param parameters: Dictionary containing the parameters.
    :return: object constructed from json.loads()
    """
    if os.environ["HMS_LOCAL"] == "True":
        url = "http://localhost:7777" + "/hms/hydrodynamic/" + submodel
    else:
        url = os.environ.get('UBERTOOL_REST_SERVER') + "/hms/hydrodynamic/" + submodel
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


def compare_input_page_errors(request, model='', header='', form=''):
    """
    Constructs html for precip compare page, with input errors.
    :param request: current request object
    :param model: current model
    :param header: current header
    :param form: form where error was found
    :return: string formatted as html
    """
    description = ""
    if model == "precip_compare":
        from hms_app.models.precip_compare import views as precip_compare_view
        description = precip_compare_view.description
    elif model == "runoff_compare":
        from hms_app.models.runoff_compare import views as runoff_compare_view
        description = runoff_compare_view.description
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header,
        'TEXT_PARAGRAPH': description
    })
    html += render_to_string('07ubertext_end_drupal.html', {})

    # -------------------- Form with Errors ---------------- #
    if model == "precip_compare":
        from hms_app.models.precip_compare import precip_compare_inputs as pc_inputs
        html += pc_inputs.precip_compare_input_page(request, model, header, form)
    elif model == "runoff_compare":
        import hms_app.models.runoff_compare.runoff_compare_inputs as rc_inputs
        html += rc_inputs.runoff_compare_input_page(request, model, header, form)

    # ----------------------- end of Form ------------------ #
    html += links_left.ordered_list(model, "")
    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html


def hydrodynamic_input_page_errors(request, model='', submodel='', header='', form=''):
    """
    Constructs the html for the hydrology input pages, containing errors in the form.
    :param request: current request object
    :param model: current model
    :param submodel: current submodel
    :param header: current header
    :param form: Previous form data.
    :return: returns a string formatted as html
    """
    import hms_app.views.hydrodynamic_submodels as hydro_sub
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
    import hms_app.models.hydrodynamic.hydrodynamic_inputs as hydrod_form
    html += hydrod_form.hydrodynamic_input_page(request, model, submodel, header, form)
    # ------------------ end of Form ----------------- #
    html += links_left.ordered_list(model, submodel)
    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html

def create_hydrodynamic_output_page(model, submodel, data, dataset):
    """
    Generates the html for the hydrodynamic output page.
    :param model: model of the data
    :param submodel: submodel of the data
    :param data: json object of the data
    :param dataset: dataset name, may be the same as submodel
    :return: string structured as html.
    """
    html = render_to_string('01hms_output_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': "HMS " + model
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    html += render_to_string('04hms_met_output.html', {
        'MODEL': model,
        'SUBMODEL': submodel,
        'TITLE': "HMS " + model.replace('_', ' ').title(),
        #'COLUMN_HEADERS': str(data['metadata']['columns']).split(", "),
        'DATA_ROWS': data['data'],
        'DATA': data#,
        #'METADATA': data['metadata'],
        #'DATASET': dataset
    })

    # Generates html for links left
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, submodel)

    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    html += render_to_string('04hms_met_output_imports.html', {})
    return html