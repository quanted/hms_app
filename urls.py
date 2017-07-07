#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf import settings
from django.conf.urls import include, url
from .views import description, landing, hydrology_submodels, output, watershed_map
from .views import runoff_compare_setup, precip_compare_setup, geometry_utils

if settings.IS_PUBLIC:
    urlpatterns = [
        #url(r'^api/', include('api.urls')),
        #url(r'^rest/', include('REST.urls')),
        url(r'^$', landing.hms_landing_page),
        #url(r'^$', views.qed_splash_page_intranet),
        # url(r'^admin/', include(admin.site.urls)),
    ]
else:
    urlpatterns = [
        #url(r'^api/', include('api.urls')),
        #url(r'^rest/', include('REST.urls')),
        url(r'^$', landing.hms_landing_page),
        url(r'^precip_compare/$', precip_compare_setup.input_page),
        url(r'^precip_compare/output/?$', output.precip_compare_output_page),
        url(r'^runoff_compare/$', runoff_compare_setup.input_page),
        url(r'^runoff_compare/output/$', output.runoff_compare_output_page),
        url(r'^(?P<model>\w+)/$', description.description_page),
        #url(r'^(?P<model>.*?)/description/?$', description.description_page),
        url(r'^hydrology/(?P<submodel>\w+)/$', hydrology_submodels.submodel_page),
        #url(r'^hydrology/(?P<submodel>\w+)/error/$', hydrology_submodels.submodel_page_error),
        url(r'^hydrology/(?P<submodel>\w+)/output/?$', output.hydrology_output_page),
        url(r'^watershed$', watershed_map.hms_map_page),
        url(r'^geometry_utils$', geometry_utils.form_page),

        #url(r'^$', views.qed_splash_page_intranet),
        #url(r'^admin/', include(admin.site.urls)),

        # rest urls
        #url(r'^rest$', hms_rest_api.pass_to_hms, name='hms_post_rest'),
        #url(r'^rest/(?P<submodel>w+)$', hms_rest_api.pass_post_to_hms, name='hms_submodel_post_rest'),
        #url(r'rest/(?P<submodel>w+)/(<parameters>)', hms_rest_api.pass_get_to_hms, name='hms_submodel_get_rest'),
        #url(r'^rest/precip_compare$', hms_rest_api.pass_precip_compare_to_hms, name='hms_precip_compare_rest')
    ]

# 404 Error view (file not found)
handler404 = landing.file_not_found
# 500 Error view (server error)
handler500 = landing.file_not_found
# 403 Error view (forbidden)
handler403 = landing.file_not_found