from rest_framework import serializers
from models import Video_clip


class Video_clip_serializer(serializers.ModelSerializer):
    class Meta:
        model = Video_clip
        fields = ['title', 'description', 'create_time', 'user']