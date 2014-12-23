from django.conf.urls import *
from django.contrib import admin
from rest_framework import routers
from registeration import urls as reg_urls
from userlocation import urls as user_loc_urls
#router = routers.DefaultRouter()
#router.register(r'users', regviews.RegisteredUserViewSet)
#router.register(r'user_list', regviews.user_list)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include(reg_urls)),
    url(r'^location/', include(user_loc_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

