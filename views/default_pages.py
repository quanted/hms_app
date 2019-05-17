from django.template.loader import render_to_string
from django.http import HttpResponse
import hms_app.views.links_left as links_left
import os


def build_model_page(request, model, submodel, title=None, import_block=None, description=None, input_block=None, algorithms=None):
    """
    Compiles model/submodel page for hms
    :param request:
    :param model:
    :param submodel:
    :param title:
    :param import_block:
    :param description:
    :param input_block:
    :param algorithms:
    :return:
    """
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA"
    imports = render_to_string('hms_default_imports.html')
    if import_block is not None:
        imports += import_block

    disclaimer_file = open(os.path.join(os.environ['PROJECT_PATH'], 'hms_app/views/disclaimer.txt'), 'r')
    disclaimer_text = disclaimer_file.read()

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Hydrologic Micro Services",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports,
        'DISCLAIMER': disclaimer_text
    })
    html += links_left.ordered_list(model=model, submodel=submodel)
    if input_block is None and algorithms is None:
        html += render_to_string('05hms_body_start.html', {
            'TITLE': title,
            'DESCRIPTION': description
        })
    else:
        html += render_to_string('05hms_body_start_2.html', {
            'TITLE': title,
            'DESCRIPTION': description,
            'INPUT_FORM': input_block,
            'ALGORITHMS': algorithms
        })
    html += render_to_string('06hms_body_end.html')
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    return html


def error_404_page(request):
    """
    Compiles model/submodel page for hms
    :param request:
    :param model:
    :param submodel:
    :param title:
    :param import_block:
    :param description:
    :param input_block:
    :param algorithms:
    :return:
    """
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA"
    imports = render_to_string('hms_default_imports.html')
    description = "The requested page was not found."
    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Hydrologic Micro Services",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports
    })
    html += links_left.ordered_list(model="", submodel="")
    html += render_to_string('05hms_body_start.html', {
        'TITLE': "Page Not Found",
        'DESCRIPTION': description
    })
    html += render_to_string('06hms_body_end.html')
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    response = HttpResponse()
    response.write(html)
    return response
