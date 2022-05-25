from django.db import models


class User(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Subscription(models.Model):
    members = models.ManyToManyField(
        User,
        through='User_has_subscription',
        through_fields=('subscription','user'),
    )

class User_has_subscription(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Ban(models.Model):
    banned = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)


class Like(models.Model):
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)


class Video_clip(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=240)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_clip = models.ForeignKey(Video_clip, on_delete=models.CASCADE)