from django.contrib import admin
from video_hosting.models import Video, Comment, User

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(User)
