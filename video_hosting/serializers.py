from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import Video, Comment, HashTag, VideoRecommendation, User, Subscriptions


class UserCreateCustomSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'owner', 'content', 'likes_count', 'created', 'video')


class VideoSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'name', 'title', 'uploaded', 'likes_count', 'user', 'link', 'comments')


class VideoFullSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('link',)
        model = Video


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = "__all__"


class VideoRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoRecommendation
        fields = "__all__"


class SubscriptionsListSerializer(serializers.ModelSerializer):
    subscriber_name = serializers.ReadOnlyField(source='subscriber.full_name')
    owner_name = serializers.ReadOnlyField(source='owner.full_name')

    class Meta:
        model = Subscriptions
        fields = ('id', 'subscriber_id', 'subscriber_name', 'owner_id', 'owner_name')


class SubscriptionsSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.full_name')

    class Meta:
        model = Subscriptions
        fields = ('id', 'owner_id', 'owner_name')


class SubscribersSerializer(serializers.ModelSerializer):
    subscriber_name = serializers.ReadOnlyField(source='subscriber.full_name')

    class Meta:
        model = Subscriptions
        fields = ('id', 'subscriber_id', 'subscriber_name')
