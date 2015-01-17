from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template

# Error handling
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import Http404

try: import simplejson as json
except ImportError: import json


def error_key(request):
    """
    If any key based error founds 
    """
    return render_to_response('keyerror.html',{'reason':'blob'},RequestContext(request))


def home(request):
    return render_to_response('general/home.html',{'page':'home'},RequestContext(request))  


def about(request):
    return render_to_response('general/about.html',{'page':'about'},RequestContext(request))
