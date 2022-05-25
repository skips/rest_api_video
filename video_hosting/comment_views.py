from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework import generics
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @method_decorator(cache_page(60 * 2))
    @method_decorator(vary_on_headers("Authorization", ))
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
