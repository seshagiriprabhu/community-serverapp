from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import generics, filters, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from userphonedata.models import UserPhoneData
from userphonedata.serializers import UserPhoneDataSerializer
from userphonedata.serializers import UserPhoneDataListSerializer
from userphonedata.serializers import UserPhoneDataDetailsSerializer


class UserPhoneDataViewSet(generics.ListCreateAPIView):
    """
    (Graphical) API endpoint that allows user phone data 
    to be added or viewed
    """
    serializer_class = UserPhoneDataSerializer
    permission_classes = (IsAdminUser,)
    
    def get(self, request, *args, **kwargs):
        queryset = UserPhoneData.objects.all()
        serializer = UserPhoneDataListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserPhoneDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPhoneDataList(generics.RetrieveAPIView):
    serializer_class = UserPhoneDataListSerializer
    permission_classes = (IsAdminUser,)
    def get(self, request, *args, **kwargs):
        queryset = UserPhoneData.objects.all()
        serializer = UserPhoneDataListSerializer(queryset, many=True)
        return Response(serializer.data)


class UserPhoneDataDetails(APIView):
    serializer_class = UserPhoneDataDetailsSerializer
    def get_object(self, uid):
        try:
            return UserPhoneData.objects.get(uid=uid)
        except UserPhoneData.DoesNotExist:
            raise Http404

    def get(self, request, uid, format=None):
        queryset = self.get_object(uid)
        serializer = UserPhoneDataDetailsSerializer(queryset)
        return Response(serializer.data)

