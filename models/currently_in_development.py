"""
HMS Feature Currently in Development
"""

from django.template.loader import render_to_string


def currently_in_development_page(request, model='', header='', form_data=None):
    """
    Constructs currently in development html page.
    :param request: current request object
    :param model: current model
    :param header: current header
    :param form_data: Set to None
    :return: string formatted as html
    """
    html = render_to_string("currently_in_development.html")
    return html

