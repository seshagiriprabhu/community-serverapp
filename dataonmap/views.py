from django.shortcuts import render_to_response
from django.template import RequestContext
from geofence.models import Geofence

def error_key(request):
    """
    If any key based error founds 
    """
    return render_to_response('keyerror.html',\
            {'reason':'blob'},RequestContext(request))


def home(request):
    geofence_list = Geofence.objects.all() 
    dbdata = []
    for geofence in geofence_list:
        dbdata.append([str(geofence.fence_name),\
                float(geofence.latitude), float(geofence.longitude),\
                float(geofence.geofence_radius)])
    return render_to_response('general/home.html',\
        {'dbdata':dbdata},RequestContext(request)) 


def about(request):
    return render_to_response('general/about.html',\
            {'page':'about'},RequestContext(request))
