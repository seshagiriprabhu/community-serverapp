from django.shortcuts import HttpResponseRedirect, render
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template

# Error handling
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import Http404

try: import simplejson as json
except ImportError: import json

from geofence.models import Geofence

def error_key(request):
    """
    If any key based error founds 
    """
    return render_to_response('keyerror.html',\
            {'reason':'blob'},RequestContext(request))


def home(request):
    geofence_list = []
    geofence_list = Geofence.objects.all() 
    return render_to_response('general/home.html',\
            {'geofence_list':geofence_list},RequestContext(request)) 


def about(request):
    return render_to_response('general/about.html',\
            {'page':'about'},RequestContext(request))
