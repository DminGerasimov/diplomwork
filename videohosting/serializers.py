from rest_framework import serializers
from videohosting import models


class Video_clip_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video_clip
        fields = ['pk', 'title', 'description', 'create_time', 'user']


class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['pk', 'name', 'surname', 'create_time']


class Ban_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ban
        fields = ['banned', 'user']


class Like_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = ['like', 'dislike', 'user']


class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['pk', 'title', 
                'description',
                'create_time',
                'user',
                'video_clip']


class Participant_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Participant
        fields = ['subscription', 'user', 'actor']

