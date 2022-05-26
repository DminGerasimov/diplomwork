from rest_framework import routers
from views import Video_clip_view_set

router = routers.DefaultRouter()
router.register(r'videoclips', Video_clip_view_set)
