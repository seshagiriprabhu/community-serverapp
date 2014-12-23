from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from registeration import views

urlpatterns = [
    url(r'^$', views.RegisteredUserViewSet.as_view(), name='user-list'),
    url(r'^user_list/$', views.user_list),
    url(r'^friend_list/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', views.friend_list),
    url(r'^friend_details/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', views.friend_details),
]
