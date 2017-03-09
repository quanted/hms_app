"""
Hydrology module views
"""
from django.template.loader import render_to_string

header = 'HMS: Hydrology'

description = '<p>Hydrology landing page under development.</p>'

baseflow_description = "<p>Base flow module under development.</p>"
evapotranspiration_description = "<p>Evapotranspiration module under development.</p>"
precipitation_description = "<p>Precipitation module under development.</p>"
soilmoisture_description = "<p>Soil moisture module under development.</p>"
surfaceflow_description = "<p>Surface flow module under development.</p>"
temperature_description = "<p>Temperature module under development.</p>"


"""
Precipitation description and input page.
"""
def hydrology_precipitation_page(request, model='', header='', form_data=None):
    import hms_app.models.hydrology.hydro_precip_parameters as precip_param
    html = render_to_string('04uberinput_start_drupal.html', {
        'MODEL': model,
        'TITLE': header})
    html += render_to_string('04uberinput_form.html', {
        'FORM': precip_param.PrecipInput(form_data)})
    html += render_to_string('04uberinput_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    return html