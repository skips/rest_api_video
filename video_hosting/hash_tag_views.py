from rest_framework import generics
from .models import HashTag
from .pagination import HashTagPagination
from .serializers import HashTagSerializer


class HashTagList(generics.ListCreateAPIView):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer
    pagination_class = HashTagPagination


class HashTagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer
