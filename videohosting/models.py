from django.db import models


class User(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class Subscription(models.Model):
    subsciber = models.ManyToManyField(
        User,
        through='Participant',
        through_fields=('subscription', 'user'),
    )

    def __str__(self):
        return f'Подписка {self.id}'

# Промежуточная таблица отношения M2M
class Participant(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    # Пользователь, объект подписки
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    # Пользователь, владелец подписки
    actor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='participant_actor',
    )

    def __str__(self):
        return f'participant={self.id} subscription={self.subscription.id} user={self.user} actor={self.actor}'


class Video_clip(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Ban(models.Model):
    banned = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)


class Like(models.Model):
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)


class Comment(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=240)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_clip = models.ForeignKey(Video_clip, on_delete=models.CASCADE)
