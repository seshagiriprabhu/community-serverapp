from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from userphonedata.models import UserPhoneData
from userphonedata.serializers import UserPhoneDataSerializer
from userphonedata.serializers import UserPhoneDataListSerializer
from userphonedata.serializers import UserPhoneDataDetailsSerializer


class UserPhoneDataViewSet(generics.CreateAPIView):
    queryset = UserPhoneData
    serializer_class = UserPhoneDataSerializer


class UserPhoneDataListViewSet(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserPhoneData.objects.all()\
            .order_by('date_time')\
            .reverse()[:5]
    serializer_class = UserPhoneDataListSerializer


class UserPhoneDataNameSearchListViewSet(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserPhoneDataDetailsSerializer
    def get_queryset(self):
        return UserPhoneData.objects\
                .filter(email=self.kwargs['pk'])\
                .order_by('date_time')\
                .reverse()


class UserPhoneDataDetailsViewSet(generics.RetrieveAPIView):
    queryset = UserPhoneData.objects.all()
    serializer_class = UserPhoneDataDetailsSerializer
