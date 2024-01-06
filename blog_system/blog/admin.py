from django.contrib import admin
from .models import Post, Comment, User

from django.contrib.auth.models import Group

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)

admin.site.unregister(Group)

