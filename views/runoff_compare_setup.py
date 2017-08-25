"""
HMS Runoff Comparision page functions
"""

from django.http import HttpResponse
import hms_app.models.runoff_compare.views as runoff_compare_view
import hms_app.views.precip_compare_setup as compare_setup


def input_page(request, header='none'):
    """
    Constructs complete input page for runoff compare
    :param request: current request object
    :param header: current header set to none
    :return: HttpResponse object
    """
    header = runoff_compare_view.header
    html = compare_setup.build_page(request, "runoff_compare", header)
    response = HttpResponse()
    response.write(html)
    return response
