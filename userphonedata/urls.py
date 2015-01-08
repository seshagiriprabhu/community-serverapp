from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from userphonedata import views

urlpatterns = [
    url(r'^$',
        views.UserPhoneDataViewSet.as_view(),
        name='user-phone-data'),
    url(r'^list/$',
        views.UserPhoneDataListViewSet.as_view(),
        name='user-phone-data-list'),
    url(r'^list/(?P<pk>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
        views.UserPhoneDataNameSearchListViewSet.as_view(),
        name='user-phone-data-list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.UserPhoneDataDetailsViewSet.as_view(),
        name='user-phone-data-details'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
