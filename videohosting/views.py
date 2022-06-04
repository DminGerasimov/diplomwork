from rest_framework import viewsets
from videohosting import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

class Video_clip_view_set(viewsets.ModelViewSet):
    queryset = models.Video_clip.objects.all()
    serializer_class = serializers.Video_clip_serializer
    filter_backends = [DjangoFilterBackend]
    # Фильтрация по параметрам в строке запроса: ...videclips?user=1&create_time="2022...
    filterset_fields = ['user', 'create_time']


class User_view_set(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.User_serializer
    filter_backends = [DjangoFilterBackend]
    # Фильтрация по параметрам в строке запроса: ...videclips?name=User1&create_time="2022...
    filterset_fields = ['name', 'create_time']
    permission_classes = [permissions.IsAuthenticated]
class Ban_view_set(viewsets.ModelViewSet):
    queryset = models.Ban.objects.all()
    serializer_class = serializers.Ban_serializer
    filter_backends = [DjangoFilterBackend]
    # Фильтрация по параметрам в строке запроса: ...bans?user=1&banned=true
    filterset_fields = ['banned', 'user']

class Like_view_set(viewsets.ModelViewSet):
    queryset = models.Like.objects.all()
    serializer_class = serializers.Like_serializer
    filter_backends = [DjangoFilterBackend]
    # Фильтрация по параметрам в строке запроса: ...likes?like=12&dislike=2&user=1
    filterset_fields = ['like', 'dislike', 'user']


class Comment_view_set(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.Comment_serializer
    filter_backends = [DjangoFilterBackend]
    # Фильтрация по параметрам в строке запроса: ...comments?user=1&video_clip=1...
    filterset_fields = ['create_time', 'user', 'video_clip']


class Participant_view_set(viewsets.ModelViewSet):
    queryset = models.Participant.objects.all()
    serializer_class = serializers.Participant_serializer
    filter_backends = [DjangoFilterBackend]
    # Фильтрация по параметрам в строке запроса: ...participant?user=1&actor=1&subscription=2
    filterset_fields = ['subscription', 'user', 'actor']