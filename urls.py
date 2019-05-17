#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.urls import path, re_path
from .views import landing, watershed_map
from .views import precip_compare_setup, api_doc, documentation, hms_model_router
from . import hms_rest_api

urlpatterns = [
    # django 2.0
    path('', landing.hms_landing_page),

    path('workflow/precip_compare/', precip_compare_setup.precip_compare_page),
    path('workflow/precip_data_extraction/', precip_compare_setup.precip_extraction_page),

    path('docs/', documentation.docs_page),
    path('hydrology/streamflow/', watershed_map.hms_workflow_page),
    path('api_doc/', api_doc.create_swagger_docs),
    path('api_doc/swagger/', api_doc.get_swagger_json),
    path('<slug:model>/', hms_model_router.component_page),

    # path('rest/watershed_delineation', hms_rest_api.delineate_watershed),
    re_path('rest/api/v2/(?P<flask_url>.*?)/?$', hms_rest_api.flask_proxy),
    re_path('rest/api/v3/(?P<model>.*?)/?$', hms_rest_api.flask_proxy_v3),
    re_path('rest/api/(?P<module>.*?)/?$', hms_rest_api.pass_through_proxy),

    # path('model/<slug:model>', hms_model_router.landing_page),
    path('<slug:model>/<slug:submodel>/', hms_model_router.component_page)
]

# 404 Error view (file not found)
handler404 = landing.file_not_found
# 500 Error view (server error)
handler500 = landing.file_not_found
# 403 Error view (forbidden)
handler403 = landing.file_not_found
