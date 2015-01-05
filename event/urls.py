from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from event import views

urlpatterns =  [
        url(r'^$',
            views.EventViewSet.as_view(),
            name='event'),
        url(r'^list/$',
            views.EventListViewSet.as_view(),
            name='event-list'),
        url(r'^list/(?P<event_id>[0-9]+)/$',
            views.EventDetailsViewSet.as_view(),
            name='event-details'),
        url(r'^attendance/$',
            views.EventAttendanceViewSet.as_view(),
            name='event-attendance'),
        url(r'^attendance/list/$',
            views.EventAttendanceListViewSet.as_view(),
            name='event-attendance-list'),
        url(r'^attendance/list/(?P<event_id>[0-9]+)$',
            views.EventAttendanceDetailsViewSet.as_view(),
            name='event-attendance-details'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
