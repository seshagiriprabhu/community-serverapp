from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from userlocation import views

urlpatterns = [
    url(r'^$', views.UserLocationViewSet.as_view()),
    url(r'^geofence/$', views.GeofenceViewSet.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
