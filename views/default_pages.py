from django.template.loader import render_to_string
from django.http import HttpResponse
import hms_app.views.links_left as ll
import os

# Paths listed in public_modules will not display the disclaimer banner at the top of the page.
# module paths, like '/hms/meteorology/precipitation/' can be added to public_modules.
public_modules = []


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

    disclaimer_file = open(os.path.join(os.environ['PROJECT_PATH'], 'views/disclaimer.txt'), 'r')
    disclaimer_text = disclaimer_file.read()
    ispublic = bool(os.getenv("HMS_RELEASE", 0))
    # notpublic = True if request.path not in public_modules else False

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Hydrologic Micro Services",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports,
        'NOTPUBLIC': not ispublic,
        'DISCLAIMER': disclaimer_text
    })
    html += ll.ordered_list(model=model, submodel=submodel)
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


def build_overview_page(request, model, submodule, title=None, import_block=None, description=None, links_left=None, top=False):
    """
    Compiles model/submodule overview page for hms
    :param request:
    :param model:
    :param submodule:
    :param title:
    :param import_block:
    :param description:
    :return:
    """
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA" + model + "," + submodule
    imports = render_to_string('hms_default_imports.html')
    if import_block is not None:
        imports += import_block

    disclaimer_file = open(os.path.join(os.environ['PROJECT_PATH'], 'views/disclaimer.txt'), 'r')
    disclaimer_text = disclaimer_file.read()
    ispublic = bool(os.getenv("HMS_RELEASE", 0))

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Hydrologic Micro Services",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports,
        'NOTPUBLIC': not ispublic,
        'DISCLAIMER': disclaimer_text
    })
    if links_left:
        html += links_left
    else:
        html += ll.ordered_list(model=model, submodel=submodule)
    if top:
        html += render_to_string("hms_module_overview_r01.html", {
            "TITLE": title,
            "DESCRIPTION": description
        })
    else:
        html += render_to_string('hms_submodule_overview_r01.html', {
            'TITLE': title,
            'MODEL': model,
            'SUBMODEL': submodule,
            'DESCRIPTION': description,
        })
    html += render_to_string('06hms_body_end.html')
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    return html


def build_input_page(request, model, submodule, title=None, import_block=None, input_block=None):
    """
    Compiles model/submodule data request page for hms
    :param request:
    :param model:
    :param submodule:
    :param title:
    :param import_block:
    :param description:
    :return:
    """
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA" + model + "," + submodule
    imports = render_to_string('hms_default_imports.html')
    if import_block is not None:
        imports += import_block

    disclaimer_file = open(os.path.join(os.environ['PROJECT_PATH'], 'views/disclaimer.txt'), 'r')
    disclaimer_text = disclaimer_file.read()
    ispublic = bool(os.getenv("HMS_RELEASE", 0))

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Hydrologic Micro Services",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports,
        'NOTPUBLIC': not ispublic,
        'DISCLAIMER': disclaimer_text
    })
    html += ll.ordered_list(model=model, submodel=submodule)
    html += render_to_string('hms_submodule_data_request_r01.html', {
        'TITLE': title,
        'MODEL': model,
        'SUBMODEL': submodule,
        'INPUT_FORM': input_block,
    })
    html += render_to_string('06hms_body_end.html')
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    return html


def build_algorithms_page(request, model, submodule, title=None, import_block=None, algorithms=None):
    """
    Compiles model/submodule algorithms page for hms
    :param request:
    :param model:
    :param submodule:
    :param title:
    :param import_block:
    :param description:
    :return:
    """
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA" + model + "," + submodule
    imports = render_to_string('hms_default_imports.html')
    if import_block is not None:
        imports += import_block

    disclaimer_file = open(os.path.join(os.environ['PROJECT_PATH'], 'views/disclaimer.txt'), 'r')
    disclaimer_text = disclaimer_file.read()
    ispublic = bool(os.getenv("HMS_RELEASE", 0))

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Hydrologic Micro Services",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports,
        'NOTPUBLIC': not ispublic,
        'DISCLAIMER': disclaimer_text
    })
    html += ll.ordered_list(model=model, submodel=submodule)
    html += render_to_string('hms_submodule_algorithms_r01.html', {
        'TITLE': title,
        'MODEL': model,
        'SUBMODEL': submodule,
        'ALGORITHMS': algorithms,
    })
    html += render_to_string('06hms_body_end.html')
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    return html

def build_output_page(request, model, submodule, title=None, import_block=None, task_id=None, advanced=False, output_block=None):
    """
    Compiles model/submodule data request page for hms
    :param request:
    :param model:
    :param submodule:
    :param title:
    :param import_block:
    :param description:
    :return:
    """
    keywords = "HMS, Hydrology, Hydrologic Micro Services, EPA" + model + "," + submodule
    imports = render_to_string('hms_default_imports.html')
    if import_block is not None:
        imports += import_block

    disclaimer_file = open(os.path.join(os.environ['PROJECT_PATH'], 'views/disclaimer.txt'), 'r')
    disclaimer_text = disclaimer_file.read()
    ispublic = bool(os.getenv("HMS_RELEASE", 0))

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Hydrologic Micro Services",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports,
        'NOTPUBLIC': not ispublic,
        'DISCLAIMER': disclaimer_text
    })
    html += ll.ordered_list(model=model, submodel=submodule)
    url = request._current_scheme_host
    html += render_to_string('hms_submodule_output_r01.html', {
        'TITLE': title,
        'MODEL': model,
        'SUBMODEL': submodule,
        'TASK_ID': task_id,
        'ADVANCED': advanced,
        'OUTPUT': output_block,
        'URL': url,
    })
    html += render_to_string('06hms_body_end.html')
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    return html


def build_map_model_page(request, model, submodel, title=None, import_block=None, description=None, input_block=None, algorithms=None):
    """
    Compiles model/submodel map page for hms
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

    disclaimer_file = open(os.path.join(os.environ['PROJECT_PATH'], 'views/disclaimer.txt'), 'r')
    disclaimer_text = disclaimer_file.read()
    notpublic = True if request.path not in public_modules else False

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': "HMS: Hydrologic Micro Services",
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': '',
        'NOTPUBLIC': notpublic,
        'DISCLAIMER': disclaimer_text
    })
    html += ll.ordered_list(model=model, submodel=submodel)
    html += render_to_string('05hms_map_body_start_2.html', {
            'TITLE': title,
            'DESCRIPTION': description,
            'INPUT_FORM': input_block,
            'ALGORITHMS': algorithms
    })
    html += render_to_string('06hms_body_end.html', {'IMPORTS': imports})
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
    html += ll.ordered_list(model="", submodel="")
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
