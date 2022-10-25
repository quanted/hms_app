import os

#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.urls import path, re_path, include
from django.conf import settings
from hms_app.views import landing, watershed_map, workflow_setup, webapp
from django.contrib.staticfiles.views import serve
from hms_app.views import precip_compare_setup, api_doc, documentation, hms_model_router, contact, default_pages, help_page, version_history, submodule_pages
import hms_rest_api


if settings.WQ_APP:
    urlpatterns = [
        path('', landing.hms_landing_page),

        path('workflow/water_quality/', workflow_setup.water_quality_page),
        # path('workflow/time_of_travel/', submodule_pages.get_overview),

        path('docs/', documentation.docs_page),
        path('contact/', contact.contact_page),
        path('contact/comment/', contact.handle_contact_post),
        path('version_history/', version_history.versions_page),
        path('help/', help_page.help_page),

        path('api_doc/', api_doc.create_swagger_docs),
        path('api_doc/swagger/', api_doc.get_swagger_json),

        re_path('rest/api/v2/(?P<flask_url>.*?)/?$', hms_rest_api.flask_proxy),
        re_path('rest/api/v3/(?P<model>.*?)/?$', hms_rest_api.flask_proxy_v3),
        re_path('rest/api/(?P<module>.*?)/?$', hms_rest_api.pass_through_proxy),

        path('webapp/', webapp.webapp_view),
        re_path(r'^webapp/.*$', webapp.redirect_view),

        path('<slug:model>/<slug:submodule>/', submodule_pages.get_overview),
        path('<slug:model>/<slug:submodule>/overview/', submodule_pages.get_overview),
        path('<slug:model>/<slug:submodule>/data_request/', submodule_pages.get_data_request),
        path('<slug:model>/<slug:submodule>/output_data/', submodule_pages.get_output_request),
        path('<slug:model>/<slug:submodule>/output_data/<slug:task_id>/', submodule_pages.get_output_request),
        path('<slug:model>/<slug:submodule>/algorithms/', submodule_pages.get_algorithms),
    ]
else:
        urlpatterns = [
        path('', landing.hms_landing_page),

        path('workflow/water_quality/', workflow_setup.water_quality_page),
        # path('workflow/time_of_travel/', workflow_setup.time_of_travel_page),

        path('docs/', documentation.docs_page),
        path('contact/', contact.contact_page),
        path('contact/comment/', contact.handle_contact_post),
        path('version_history/', version_history.versions_page),
        path('help/', help_page.help_page),

        path('api_doc/', api_doc.create_swagger_docs),
        path('api_doc/swagger/', api_doc.get_swagger_json),

        re_path('rest/api/v2/(?P<flask_url>.*?)/?$', hms_rest_api.flask_proxy),
        re_path('rest/api/v3/(?P<model>.*?)/?$', hms_rest_api.flask_proxy_v3),
        re_path('rest/api/(?P<module>.*?)/?$', hms_rest_api.pass_through_proxy),

        path('<slug:model>/<slug:submodule>/', submodule_pages.get_overview),
        path('<slug:model>/<slug:submodule>/overview/', submodule_pages.get_overview),
        path('<slug:model>/<slug:submodule>/data_request/', submodule_pages.get_data_request),
        path('<slug:model>/<slug:submodule>/output_data/', submodule_pages.get_output_request),
        path('<slug:model>/<slug:submodule>/output_data/<slug:task_id>/', submodule_pages.get_output_request),
        path('<slug:model>/<slug:submodule>/algorithms/', submodule_pages.get_algorithms),
    ]

urlpatterns = [path('hms/', include(urlpatterns))]

# 404 Error view (file not found)
handler404 = landing.file_not_found
# 500 Error view (server error)
handler500 = landing.file_not_found
# 403 Error view (forbidden)
handler403 = landing.file_not_found
