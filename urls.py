#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path, re_path
from .views import description, landing, hydrology_submodels, output, watershed_map, meteorology_submodels
from .views import runoff_compare_setup, precip_compare_setup, water_quality_submodels, api_doc
from .models.water_quality import output as wq_output
from . import hms_rest_api

if settings.IS_PUBLIC:
    urlpatterns = [
        # url(r'^api/', include('api.urls')),
        # url(r'^rest/', include('REST.urls')),
        url(r'^$', landing.hms_landing_page),
        # url(r'^$', views.qed_splash_page_intranet),
        # url(r'^admin/', include(admin.site.urls)),
    ]
else:
    urlpatterns = [

        # django 1.11
        # url(r'^$', landing.hms_landing_page),
        # url(r'^precip_compare/$', precip_compare_setup.input_page),
        # url(r'^precip_compare/output/?$', output.precip_compare_output_page),
        # url(r'^runoff_compare/$', runoff_compare_setup.input_page),
        # url(r'^runoff_compare/output/$', output.runoff_compare_output_page),
        # url(r'^hydrology/(?P<submodel>\w+)/$', hydrology_submodels.submodel_page),
        # url(r'^hydrology/(?P<submodel>\w+)/output/?$', output.hydrology_output_page),
        # url(r'^water_quality/(?P<submodel>\w+)/$', water_quality_submodels.submodel_page),
        # url(r'^water_quality/(?P<submodel>\w+)/output$', wq_output.water_quality_output),
        # url(r'^water_quality/(?P<submodel>\w+)/output/json$', wq_output.water_quality_json_output),
        # url(r'^watershed$', watershed_map.hms_map_page),
        # url(r'^api_doc/$', api_doc.create_swagger_docs),
        # url(r'^api_doc/swagger$', api_doc.get_swagger_json),
        # url(r'^(?P<model>\w+)/$', description.description_page),

        # django 2.0
        path('', landing.hms_landing_page),
        path('precip_compare/', precip_compare_setup.input_page),
        path('precip_compare/output/', output.precip_compare_output_page),
        path('runoff_compare/', runoff_compare_setup.input_page),
        path('runoff_compare/output/', output.runoff_compare_output_page),
        path('hydrology/<slug:submodel>/', hydrology_submodels.submodel_page),
        path('hydrology/<slug:submodel>/output/', output.hydrology_output_page),
        path('meteorology/<slug:submodel>/', meteorology_submodels.submodel_page),
        path('meteorology/<slug:submodel>/output/', output.meteorology_output_page),
        path('water_quality/<slug:submodel>/', water_quality_submodels.submodel_page),
        path('water_quality/<slug:submodel>/output/', wq_output.water_quality_output),
        path('water_quality/<slug:submodel>/output/json/', wq_output.water_quality_json_output),
        path('watershed_workflow/', watershed_map.hms_map_page),
        path('api_doc/', api_doc.create_swagger_docs),
        path('api_doc/swagger/', api_doc.get_swagger_json),
        path('<slug:model>/', description.description_page),

        path('rest/watershed_delineation', hms_rest_api.delineate_watershed),
        re_path('rest/api/(?P<module>.*?)/?$', hms_rest_api.pass_through_proxy)
    ]

# 404 Error view (file not found)
handler404 = landing.file_not_found
# 500 Error view (server error)
handler500 = landing.file_not_found
# 403 Error view (forbidden)
handler403 = landing.file_not_found