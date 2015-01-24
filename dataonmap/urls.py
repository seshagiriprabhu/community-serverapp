from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from dataonmap import views

urlpatterns = [
    url(r'^about/$', views.about),
    url(r'^geofence/$',
        views.get_geofence,
        name='geofence-data'),
    url(r'^location/$',
        views.get_userlocation,
        name='user-location'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
