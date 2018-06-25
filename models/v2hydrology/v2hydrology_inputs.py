"""
HMS Hydrology Input form function
"""

from django.template.loader import render_to_string


def v2hydrology_input_page(request, model='', submodel='', header='', form_data=None):
    """
    Constructs the html for the hydrology input pages.
    :param request: current request object
    :param model: current model
    :param submodel: current submodel
    :param header: current header
    :param form_data: Set to None
    :return: returns a string formatted as html
    """
    sub_import = "/static_qed/hms/js/hydrology/hms_" + submodel + ".js"
    html = render_to_string('04hms_js_imports.html', {
        'SUBMODEL_IMPORT': sub_import
    })
    html += render_to_string('04hms_input_start_drupal.html',
                             {
                                 'MODEL': model,
                                 'SUBMODEL': submodel,
                             },
                             request=request)
    # request object passed to render_to_string to test for csrf handling
    if (form_data is None):
        submodel_form = get_submodel_form_input(submodel, form_data)
        html += render_to_string('04uberinput_form.html', {
            'FORM': submodel_form, })
    else:
        html += render_to_string('04hms_input_form.html', {
            'FORM': form_data, })
    html += render_to_string('04uberinput_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    return html


def get_submodel_form_input(submodel, form_data):
    """
    Gets the input form for the specified submodel.
    :param submodel: current submodel
    :param form_data: existing form data, currently set to None
    :return: returns django Form object
    """
    from ..v2hydrology import v2hydrology_parameters as hp

    if submodel == 'subsurfaceflow':
        return hp.SubsurfaceflowFormInput(form_data)
    #elif submodel == 'precipitation':
        #return hp.PrecipitationFormInput(form_data)
    elif submodel == 'evapotranspiration':
        return hp.EvapotranspirationFormInput(form_data)
    elif submodel == 'soilmoisture':
        return hp.SoilmoistureFormInput(form_data)
    elif submodel == 'surfacerunoff':
        return hp.SurfacerunoffFormInput(form_data)
    #elif submodel == "temperature":
        #return hp.TemperatureFormInput(form_data)
    else:
        return ''
