from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, filters, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from registeration.models import Registeration
from registeration.serializers import RegisterationSerializer
from registeration.serializers import FriendListSerializer
from registeration.serializers import FriendDetailSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class RegisteredUserViewSet(generics.ListCreateAPIView):
    """
    (Graphical) API endpoint that allows users to be viewed or added.
    """
    queryset = Registeration.objects.all()
    serializer_class = RegisterationSerializer
    permission_classes = (IsAdminUser,)
    
    def get_paginate_by(self):
        """
        Use smaller pagination for HTML representation
        """
        if self.request.accepted_renderer.format == 'html':
            return 20
        return 100

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RegisterationSerializer(queryset, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        user_list = Registeration.objects.all()
        serializer = RegisterationSerializer(user_list, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def friend_list(request, email):
    try:
        user = Registeration.objects.get(email=email)
    except Registeration.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        user_list = Registeration.objects.all()
        friend_list = []
        for user in user_list:
            if user.email != email:
                friend_list.append(user)
        serializer = FriendListSerializer(friend_list, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
@api_view(['GET'])
def friend_details(request, email):
    try:
        user = Registeration.objects.get(email=email)
    except Registeration.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = FriendDetailSerializer(user)
        return JSONResponse(serializer.data)
