from rest_framework import generics
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from datetime import datetime, timedelta

# Models from user defined apps
from dataonmap.models import UserGeoLocation
from geofence.models import Geofence
from registeration.models import Registeration

@api_view(['GET'])
def get_userlocation(request):
    result = UserGeoLocation.objects.all().reverse()
    data = serializers.serialize('json', result)
    return Response(data, status=status.HTTP_200_OK,\
            content_type='application/json')


@api_view(['GET'])
def get_geofence(request):
    result = Geofence.objects.all()
    data = serializers.serialize('json', result)
    return Response(data, status=status.HTTP_200_OK,\
            content_type='application/json')

@api_view(['GET'])
def map_filter(request):
    request_data = request.QUERY_PARAMS
    filtered_fields = request_data['fields']
    daynight = 0
    kwargs = {}

    if "user" in filtered_fields:
        kwargs["disp_name"] = str(request_data["user"])
    if "period" in filtered_fields:
        period = request_data['period']
        start = datetime.now()
        end = start - timedelta(days=int(period))
        kwargs["date_time__gte"] = end
    if "daynight" in filtered_fields:
        if request_data['daynight'] == "day":
            daynight, start_hour, end_hour = 1, 6, 18
        else:
            daynight, start_hour, end_hour = 2, 18, 6
    try:
        result = []
        locations = UserGeoLocation.objects.filter(**kwargs)
        # Day time user activities (06:00-18:00)
        if daynight == 1:
            for location in locations:
                hour = int(location.date_time.hour)
                mins = int(location.date_time.minute)
                if hour >= start_hour and hour < end_hour:
                    result.append(location)
        # Night time user activities (08:00-06:00)
        elif daynight == 2:
            for location in locations:
                hour = int(location.date_time.hour)
                if (hour >= start_hour and hour <= 23) or\
                    (hour >= 0 and hour < end_hour):
                    result.append(location)
        # Show all user activities
        else:
            result = locations
        data = serializers.serialize('json', result)
        return Response(data, status=status.HTTP_200_OK,\
                content_type='application/json')
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def error_key(request):
    return render_to_response('keyerror.html',\
            {'reason':'blob'},RequestContext(request))


def home(request):
    users=[]
    registeration = Registeration.objects.all()
    for user in registeration:
        users.append(user.display_name)
    return render_to_response('general/home.html',\
            {'users':users}, RequestContext(request)) 


def geomap(request):
    return render_to_response('general/geofences.html',\
            {}, RequestContext(request)) 


def about(request):
    return render_to_response('general/about.html',\
            {'page':'about'},RequestContext(request))
