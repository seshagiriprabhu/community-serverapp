from django.conf.urls import  patterns, include, url
from django.contrib import admin
from dataonmap import views as dataonmap_views
admin.autodiscover()

urlpatterns = [
    url(r'^$', dataonmap_views.home),
    url(r'^data_analysis/', include('dataonmap.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include('registeration.urls')),
    url(r'^location/', include('userlocation.urls')),
    url(r'^data/', include('userphonedata.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^geofence/', include('geofence.urls')),
    url(r'^api-auth/', include('rest_framework.urls',\
            namespace='rest_framework'))
]

