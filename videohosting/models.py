from django.db import models

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os

from django.contrib.auth.models import User as DjangoUser


class User(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    create_time = models.DateTimeField(auto_now_add=True)
    django_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('name',)


class Subscription(models.Model):
    subsciber = models.ManyToManyField(
        User,
        through='Participant',
        through_fields=('subscription', 'user'),
    )

    def __str__(self):
        return f'Подписка {self.id}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('pk',)


# Промежуточная таблица отношения M2M
class Participant(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    # Пользователь, объект подписки (на кого подписались)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    # Пользователь, владелец подписки (кто подписался)
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
    upload = models.FileField(upload_to='video/%Y/%m/%d/')


# Подписка на удаление медиа файла из Video_clip
@receiver(pre_delete, sender=Video_clip)
def clip_model_delete(sender, instance, **kwargs):
    if instance.upload:
        if os.path.isfile(instance.upload.path):
            os.remove(instance.upload.path)


class Ban(models.Model):
    banned = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)

    class Meta:
            verbose_name = 'Блокировка'
            verbose_name_plural = 'Блокировки'
            ordering = ('banned',)


class Like(models.Model):
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        ordering = ('like',)


class Comment(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=240)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_clip = models.ForeignKey(Video_clip, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('create_time',)
