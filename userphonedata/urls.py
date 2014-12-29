from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from userphonedata import views

urlpatterns = [
    url(r'^$',
        views.UserPhoneDataViewSet.as_view(),
        name='user-phone-data'),
    url(r'^list/$',
        views.UserPhoneDataList.as_view(),
        name='user-phone-data-list'),
    url(r'^list/(?P<uid>[0-9]+)/$',
        views.UserPhoneDataDetails.as_view(),
        name='user-phone-data-details'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
