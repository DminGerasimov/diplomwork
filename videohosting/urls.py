from rest_framework import routers
from videohosting import views

router = routers.DefaultRouter()
router.register(r'videoclips', views.Video_clip_view_set)
urlpatterns = router.urls
