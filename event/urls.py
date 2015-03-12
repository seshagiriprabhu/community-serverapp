from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from event import views

urlpatterns =  [
        url(r'^$',
            views.EventViewSet.as_view(),
            name='event'),
        url(r'^list/open/$',
            views.EventListAllOpenViewSet.as_view(),
            name='event-list'),
        url(r'^list/closed/$',
            views.EventListAllClosedViewSet.as_view(),
            name='event-list'),
        url(r'^(?P<pk>[0-9]+)/$',
            views.EventDetailsViewSet.as_view(),
            name='event-details'),
        url(r'^list/(?P<pk>[\w.%+-]+)/$',
            views.EventNameListViewSet.as_view(),
            name='event-list-name'),
        url(r'^attendance/$',
            views.EventAttendanceViewSet.as_view(),
            name='event-attendance'),
        url(r'^(?P<pk>[0-9]+)/attendance/$',
            views.EventAttendanceListViewSet.as_view(),
            name='event-attendance-list'),
        url(r'^attendance/(?P<pk>[0-9]+)/$',
            views.EventAttendanceDetailsViewSet.as_view(),
            name='event-attendance-details'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
