from rest_framework import viewsets
from models import Video_clip
from videohosting import serializers

class Video_clip_view_set(viewsets.ModelViewSet):
    queryset = Video_clip.objects.all()
    serializer_class = serializers.Video_clip_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'create_time']