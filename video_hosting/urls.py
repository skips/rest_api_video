from django.urls import path
from .subscriptions_views import SubscriptionsList, MySubscriptions, MySubscribers
from .video_views import VideoList, VideoDetail, OnlyMyVideoView
from .comment_views import CommentList, CommentDetail
from .hash_tag_views import HashTagList, HashTagDetail

urlpatterns = [
    path('videos/', VideoList.as_view()),
    path('videos/<int:pk>/', VideoDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path("hashtag/", HashTagList.as_view()),
    path("hashtag/<int:pk>/", HashTagDetail.as_view()),
    path("videos/get-my/", OnlyMyVideoView.as_view()),
    path('subscriptions/', SubscriptionsList.as_view()),
    path('subscriptions/mysubscriptions/', MySubscriptions.as_view()),
    path('subscriptions/mysubscribers/', MySubscribers.as_view()),
]
