from rest_framework import generics
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

# Models from user defined apps
from dataonmap.models import UserGeoLocation
from geofence.models import Geofence


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


def error_key(request):
    return render_to_response('keyerror.html',\
            {'reason':'blob'},RequestContext(request))


def home(request):
    return render_to_response('general/home.html',\
        RequestContext(request)) 


def about(request):
    return render_to_response('general/about.html',\
            {'page':'about'},RequestContext(request))
