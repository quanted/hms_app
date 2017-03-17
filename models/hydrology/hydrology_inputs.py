"""
Hydrology input form
"""

from django.template.loader import render_to_string

#TODO: update 04hms_input_jqery.html to dynamically change layer options for source changes.

def hydrology_input_page(request, model='', submodel='', header='', form_data=None):
    html = render_to_string('04hms_input_jquery.html', {})
    html += render_to_string('04hms_input_start_drupal.html', {
        'MODEL': model,
        'SUBMODEL': submodel,
        'TITLE': header
    })
    submodel_form = get_submodel_form_input(submodel, form_data)
    html += render_to_string('04uberinput_form.html', {
        'FORM': submodel_form, })
    html += render_to_string('04uberinput_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    return html


def get_submodel_form_input(submodel, form_data):
    import hydrology_parameters
    if( submodel == 'baseflow' ):
        return hydrology_parameters.BaseflowFormInput(form_data)
    elif( submodel == 'evapotranspiration' ):
        return hydrology_parameters.EvapotranspirationFormInput(form_data)
    elif( submodel == 'precipitation' ):
        return hydrology_parameters.PrecipitationFormInput(form_data)
    elif( submodel == 'soilmoisture' ):
        return hydrology_parameters.SoilMoistureFormInput(form_data)
    elif( submodel == 'surfacerunoff' ):
        return hydrology_parameters.SurfacerunoffFormInput(form_data)
    elif( submodel == 'temperature' ):
        return hydrology_parameters.TemperatureFormInput(form_data)
    else:
        return