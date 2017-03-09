#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf import settings
from django.conf.urls import include, url
from views import description, landing
from models.hydrology import views as hydroViews

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
        url(r'^(?P<model>.*?)/$', description.description_page),
        url(r'^(?P<model>.*?)/description/?$', description.description_page),
        url(r'^(?P<model>.*?)/precipitation/?$', hydroViews.hydrology_precipitation_page),

        #url(r'^$', views.qed_splash_page_intranet),
        # url(r'^admin/', include(admin.site.urls)),
    ]

# 404 Error view (file not found)
handler404 = landing.file_not_found
# 500 Error view (server error)
handler500 = landing.file_not_found
# 403 Error view (forbidden)
handler403 = landing.file_not_found
