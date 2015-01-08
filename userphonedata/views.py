from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from userphonedata.models import UserPhoneData
from userphonedata.serializers import UserPhoneDataSerializer
from userphonedata.serializers import UserPhoneDataListSerializer
from userphonedata.serializers import UserPhoneDataDetailsSerializer


class UserPhoneDataViewSet(generics.ListCreateAPIView):
    queryset = UserPhoneData.objects.all()
    serializer_class = UserPhoneDataSerializer


class UserPhoneDataList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserPhoneData.objects.all()
    serializer_class = UserPhoneDataListSerializer


class UserPhoneDataDetails(generics.RetrieveAPIView):
    queryset = UserPhoneData.objects.all()
    serializer_class = UserPhoneDataDetailsSerializer
