"""
HMS Water Quality Input form function
"""

from django.template.loader import render_to_string


def water_quality_input_page(request, model='', submodel='', header='', form_data=None):
    """
    Constructs the html for the water quality input pages.
    :param request: current request object
    :param model: current model
    :param submodel: current submodel
    :param header: current header
    :param form_data: Set to None
    :return: returns a string formatted as html
    """
    # submodel custom imports
    html = render_to_string(submodel + '_imports.html', {})

    submodel_form = get_submodel_form_input(submodel, form_data)
    html += render_to_string('04hms_water_quality_input_form.html',
                             {
                                 'FORM': submodel_form,
                                 'MODEL': model,
                                 'SUBMODEL': submodel,
                             }, request=request)

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
    from ..water_quality import water_quality_parameters as wq

    if submodel == 'photolysis':
        return wq.PhotolysisFormInput(form_data)
    else:
        return ''
