from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from userlocation import views

urlpatterns = [
    url(r'^$', 
        views.UserLocationViewSet.as_view(),
        name='user-location'),
    url(r'^list/$', 
        views.UserLocationListViewSet.as_view(),
        name='user-location-list'),
    url(r'^list/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', 
        views.UserLocationDetailsViewSet.as_view(),
        name='user-location-detail'),
    url(r'^geofence/$',
        views.GeofenceViewSet.as_view(),
        name='geofence'),
    url(r'^geofence/list/$',
        views.GeofenceListViewSet.as_view(),
        name='geofence-list'),
    url(r'^geofence/gid/(?P<gid>[0-9]+)/$',
        views.GeofenceDetailsViewSet.as_view(),
        name='geofence-gid-search'),
    url(r'^geofence/name/(?P<fence_name>[\w.%+-]+)/$',
        views.GeofenceNameSearchDetailsViewset.as_view(),
        name='geofence-name-search'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
