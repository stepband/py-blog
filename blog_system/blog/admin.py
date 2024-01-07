from django.contrib import admin

from django.contrib.auth.models import Group

from .models import Post, Commentary, User

admin.site.register(Post)
admin.site.register(Commentary)
admin.site.register(User)

admin.site.unregister(Group)