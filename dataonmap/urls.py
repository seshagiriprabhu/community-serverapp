from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from dataonmap import views

urlpatterns = [
    url(r'^about/$', views.about),
    url(r'^geofence/$',
        views.get_geofence,
        name='geofence-data'),
    url(r'^geofence/(?P<pk>[0-9]+)/$',
        views.get_geofence_details,
        name='geofence-details'),
    #url(r'^map/geofence/(?<pk>[0-9]+)/$',
    #    views.geomap,
    #    name='geofence-view'),
    url(r'^location/$',
        views.get_userlocation,
        name='user-location'),
    url(r'^location/filter/$',
        views.map_filter,
        name='map-filter'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
