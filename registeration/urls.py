from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from registeration import views

urlpatterns = [
    url(r'^$', 
        views.RegisteredUserViewSet.as_view(), 
        name='user-list'),
    url(r'^friend_list/(?P<pk>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', 
        views.FriendListViewSet.as_view(),
        name='friend-list'),
    url(r'^all_users/$', 
        views.AllRegisteredUsersViewSet.as_view(),
        name='all-users'),
    url(r'^user_details/(?P<pk>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', 
        views.UserDetailsViewSet.as_view(),
        name='user-details'),
    url(r'^user_created_events/(?P<pk>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', 
        views.UserCreatedEventsViewSet.as_view(),
        name='user-created-events'),
    url(r'^user_attended_events/(?P<pk>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', 
        views.UserAttendedEventsViewSet.as_view(),
        name='user-attended-events'),
]
