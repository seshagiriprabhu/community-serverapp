from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from geofence import urls


urlpatterns = [
    url(r'^$',
        views.GeofenceViewSet.as_view(),
        name='geofence'),
    url(r'^list/$',
        views.GeofenceListViewSet.as_view(),
        name='geofence-list'),
    url(r'^gid/(?P<gid>[0-9]+)/$',
        views.GeofenceDetailsViewSet.as_view(),
        name='geofence-gid-search'),
    url(r'^name/(?P<fence_name>[\w.%+-]+)/$',
        views.GeofenceNameSearchDetailsViewset.as_view(),
        name='geofence-name-search'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
