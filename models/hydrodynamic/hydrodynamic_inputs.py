"""
HMS Hydrodynamic Input form function
"""

from django.template.loader import render_to_string


def hydrodynamic_input_page(request, model='', submodel='', header='', form_data=None):
    """
    Constructs the html for the hydrodynamic input pages.
    :param request: current request object
    :param model: current model
    :param submodel: current submodel
    :param header: current header
    :param form_data: Set to None
    :return: returns a string formatted as html
    """
    sub_import = "/hms/static/js/hydrodynamic/hms_" + submodel + ".js"
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
    from ..hydrodynamic import hydrodynamic_parameters as hp
    # import hms_app.models.hydrodynamic.hydrodynamic_parameters as hp

    if (submodel == 'constant_volume'):
        return hp.Constant_VolumeFormInput(form_data)
    elif (submodel == 'changing_volume'):
        return hp.Changing_VolumeFormInput(form_data)
    elif (submodel == 'kinematic_wave'):
        return hp.Kinematic_WaveFormInput(form_data)
    else:
        return ''
