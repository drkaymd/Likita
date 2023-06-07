from django.contrib import admin
from .models import User, Post, Topic,LikedPost, Comment, CommentReply
# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(LikedPost)
admin.site.register(Comment)
admin.site.register(CommentReply)