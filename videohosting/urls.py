from rest_framework import routers
from videohosting import views

router = routers.DefaultRouter()
router.register(r'videoclips', views.Video_clip_view_set)
router.register(r'users', views.User_view_set)
router.register(r'bans', views.Ban_view_set)
router.register(r'likes', views.Like_view_set)
router.register(r'comments', views.Comment_view_set)
router.register(r'participants', views.Participant_view_set)
router.register(r'channelusergroup', views.ChannelUserGroup_view_set)
router.register(r'usermessage', views.UserMessage_view_set)

urlpatterns = router.urls
