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
]
urlpatterns = format_suffix_patterns(urlpatterns)
