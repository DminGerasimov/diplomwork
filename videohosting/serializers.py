from rest_framework import serializers
from videohosting import models


class Video_clip_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video_clip
        fields = ['title', 'description', 'create_time', 'user']