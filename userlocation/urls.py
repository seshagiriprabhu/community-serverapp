from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from userlocation import views

urlpatterns = [
    url(r'^$', views.UserLocationViewSet.as_view()),
    url(r'^list/$', views.user_location_details_list),
    url(r'^geofence/$', views.GeofenceViewSet.as_view()),
    url(r'^geofence/(?P<gid>[0-9]+)/$', views.GeofenceDetails.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
