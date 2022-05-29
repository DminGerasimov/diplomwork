from django.contrib import admin

from .models import User, Subscription, Participant, Ban, Like, Video_clip, Comment

admin.site.register(User)
admin.site.register(Subscription)
admin.site.register(Participant)
admin.site.register(Video_clip)
admin.site.register(Comment)
admin.site.register(Ban)
admin.site.register(Like)
