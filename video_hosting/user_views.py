from rest_framework import generics
from video_hosting.models import User
from video_hosting.serializers import UserCreateCustomSerializer


class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateCustomSerializer
