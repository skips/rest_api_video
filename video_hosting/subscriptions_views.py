from rest_framework import generics
from video_hosting.models import Subscriptions
from video_hosting.serializers import SubscriptionsListSerializer, SubscriptionsSerializer, SubscribersSerializer


class SubscriptionsList(generics.ListCreateAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsListSerializer

    def perform_create(self, serializer):
        serializer.save(subscriber=self.request.user)


class MySubscriptions(generics.ListAPIView):
    serializer_class = SubscriptionsSerializer

    def get_queryset(self):
        user = self.request.user
        return Subscriptions.objects.filter(subscriber=user)


class MySubscribers(generics.ListAPIView):
    serializer_class = SubscribersSerializer

    def get_queryset(self):
        user = self.request.user
        return Subscriptions.objects.filter(owner=user)
