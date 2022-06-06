from rest_framework import viewsets, mixins
from videohosting import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class Video_clip_view_set(  mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = models.Video_clip.objects.all()
    serializer_class = serializers.Video_clip_serializer
    filter_backends = [DjangoFilterBackend]
    # Фильтрация по параметрам в строке запроса: ...videclips?user=1&create_time="2022...
    filterset_fields = ['user', 'create_time']

    def isMyUserId(context):
        # Сравнение имени пользователя обекта из БД и имени пользователя из контекста запроса
        return str(context.get_object().user) == str(context.request.user)

    # Создание только своего контента доступно авторизованным пользователям
    def perform_create(self, serializer):
        if not self.isMyUserId():
            raise ValidationError(
                {"detail": f"permissions not available for user {str(self.request.user)}"}
            )
        serializer.save()
    # curl -u admin:admin -v  -d "title=Vc5" -X PUT http://51.250.69.126:8000/api/videoclips/

    # Обновление только своего контента доступно авторизованным пользователям
    def perform_update(self, serializer):
        self.perform_create(serializer)
    # curl -u admin:admin -v  -d "title=Video clip&description=Descriptions1" -X PATCH http://51.250.69.126:8000/api/videoclips/1/

    # Удаление только своего контента доступно авторизованным пользователям
    def perform_destroy(self, request, *args, **kwargs):
        if not self.isMyUserId():
            raise ValidationError(
                {"detail": f"permissions not available for user {str(self.request.user)}"}
            )
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # curl -u admin:admin -v  -d "title=Vc" -X DELETE http://51.250.69.126:8000/api/videoclips/1/


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
    # Фильтрация по параметрам в строке запроса: ...participants?user=1&actor=1&subscription=2
    filterset_fields = ['subscription', 'user', 'actor']