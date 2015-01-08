from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from userlocation.models import UserLocationData
from userlocation.serializers import UserLocationSerializer
from userlocation.serializers import UserLocationListSerializer
from userlocation.serializers import UserLocationDetailsSerializer


class UserLocationViewSet(generics.ListCreateAPIView):
    queryset = UserLocationData.objects.all().reverse()[:5]
    serializer_class = UserLocationSerializer    


class UserLocationDetailsViewSet(generics.RetrieveAPIView):
    queryset = UserLocationData.objects.all()
    serializer_class = UserLocationDetailsSerializer


class UserLocationListViewSet(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserLocationData.objects.all()
    serializer_class = UserLocationListSerializer
