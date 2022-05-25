from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=True, default="")
    last_name = models.CharField(max_length=100, blank=True, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(blank=False, default=False)
    delete_at = models.DateTimeField(null=True, default=None)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Video(models.Model):
    name = models.CharField(max_length=255, default="Untitled")
    title = models.CharField(max_length=255, default="Empty")
    uploaded = models.DateTimeField(auto_now_add=True, blank=True)
    likes_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE, blank=True, null=True)
    link = models.URLField(max_length=255, null=False, blank=False)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return f'{self.name}-{self.id}'


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=False, null=False, related_name="comments")
    content = models.TextField()
    likes_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.content}-{self.id}'

    class Meta:
        ordering = ['created']


class HashTag(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True, related_name="hashtag")
    tag = models.CharField(max_length=255, default="#")


class VideoRecommendation(models.Model):
    videos = models.ManyToManyField(Video, blank=True, related_name="recommendation")
    recommendation_name = models.CharField(max_length=255, default="")
    is_top_rated = models.BooleanField()


class Subscriptions(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="owner")
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="subscriber")
