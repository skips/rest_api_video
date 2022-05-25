from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer, VideoFullSerializer


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    @method_decorator(cache_page(60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        queryset = self.get_queryset()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)

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
