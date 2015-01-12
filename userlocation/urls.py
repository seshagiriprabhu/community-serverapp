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
    url(r'^(?P<pk>[0-9]+)/$', 
        views.UserLocationDetailsViewSet.as_view(),
        name='user-location-detail'),
    url(r'^gid/(?P<pk>[0-9]+)/activities/$', 
        views.GeofenceUserActivitiesViewSet.as_view(),
        name='geofence-online-users'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
