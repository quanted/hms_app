"""
HMS Meteorology Input form function
"""

from django.template.loader import render_to_string


def meteorology_input_page(request, model='', submodel='', header='', form_data=None):
    """
    Constructs the html for the meteorology input pages.
    :param request: current request object
    :param model: current model
    :param submodel: current submodel
    :param header: current header
    :param form_data: Set to None
    :return: returns a string formatted as html
    """
    sub_import = "/static_qed/hms/js/meteorology/" + submodel + ".js"
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
    from ..meteorology import meteorology_parameters as mp

    if submodel == 'solarcalculator':
        return mp.SolarcalculatorFormInput(form_data)
    else:
        return ''
