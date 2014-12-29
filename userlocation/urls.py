from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from userlocation import views

urlpatterns = [
    url(r'^$', 
        views.UserLocationViewSet.as_view(),
        name='user-location'),
    url(r'^list/$', 
        views.ListUserLocationDetails.as_view(),
        name='user-location-list'),
    url(r'^list/(?P<uid>[0-9]+)/$', 
        views.UserLocationDetails.as_view(),
        name='user-location-detail'),
    url(r'^geofence/$',
        views.GeofenceViewSet.as_view(),
        name='geofence-list'),
    url(r'^geofence/(?P<gid>[0-9]+)/$',
        views.GeofenceDetails.as_view(),
        name='geofence-details'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
