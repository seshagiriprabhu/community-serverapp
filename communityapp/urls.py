from django.conf.urls import *
from django.contrib import admin
from rest_framework import routers
from registeration import urls as reg_urls
from userlocation import urls as user_loc_urls
from userphonedata import urls as user_phone_data_urls
from event import urls as event_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include(reg_urls)),
    url(r'^location/', include(user_loc_urls)),
    url(r'^data/', include(user_phone_data_urls)),
    url(r'^event/', include(event_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
