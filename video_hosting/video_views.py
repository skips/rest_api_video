from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer, VideoFullSerializer


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class OnlyMyVideoView(generics.ListAPIView):
    serializer_class = VideoFullSerializer

    def get_queryset(self):
        user = self.request.user
        return Video.objects.filter(user=user)
