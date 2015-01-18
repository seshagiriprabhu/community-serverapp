from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime, timedelta

# Models from user defined apps
from registeration.models import Registeration
from geofence.models import Geofence
from userlocation.models import UserLocationData

def error_key(request):
    """
    If any key based error founds 
    """
    return render_to_response('keyerror.html',\
            {'reason':'blob'},RequestContext(request))


def home(request):
    """
    A view to display geofences and user location activities
    of last 24 hours
    """
    fencedata = []
    userlocationdata = []
    
    # Obtain all the geofence details
    geofence_list = Geofence.objects.all()  
    for geofence in geofence_list:
        fencedata.append(\
                [str(geofence.fence_name),\
                float(geofence.latitude),\
                float(geofence.longitude),\
                float(geofence.geofence_radius)])

    # Obtain all the user location details of last 24 hours
    userlocation_list = UserLocationData.objects\
            .filter(transition_type__lte=2,\
            date_time__gte = datetime.now() - timedelta(days=1))\
            .exclude(transition_type__lte=-1)\
            .order_by('date_time')\
            .reverse()

    for location in userlocation_list:
        current_gid = str(location.gid).partition(',')[0]
        geofence = Geofence.objects.get(gid=current_gid)
        registeration = Registeration.objects.get(email=str(location.email))
        # Converting date in ISO format to least wanted format  
        date_time = location.date_time.replace(microsecond=0, tzinfo=None)
        date_time = date_time.strftime("%H:%S on %d/%m/%y")

        if location.transition_type == 1: t_type = "Entered"
        else: t_type = "Exited"

        userlocationdata.append(\
                [str(registeration.display_name),\
                str(date_time),\
                str(t_type), 
                float(geofence.latitude),\
                float(geofence.longitude),\
                str(geofence.fence_name)])

    return render_to_response('general/home.html',\
        {'fencedata':fencedata,\
        'userlocationdata':userlocationdata,\
        },RequestContext(request)) 


def about(request):
    return render_to_response('general/about.html',\
            {'page':'about'},RequestContext(request))
