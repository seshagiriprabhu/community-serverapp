from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from dataonmap import views

urlpatterns = patterns('',
        (r'^$', views.home),
        (r'^about/$', views.about),
)
urlpatterns = format_suffix_patterns(urlpatterns)
