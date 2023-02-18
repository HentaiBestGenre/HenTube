from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ChannelTags(models.Model):
    value = models.TextField(max_length=20)


class Channels(models.Model):
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    description = models.TextField(max_length=300, null=True, default=None)
    creation_date = models.DateTimeField("creation date", default=timezone.now)
    tags = models.ManyToManyField(ChannelTags, null=True)
    subscribers = models.BigIntegerField(default=0)

    def __str__(self):
        return f'id: {self.user_id}, creation date: {self.creation_date}'

    def add_subscriber(self, value):
        self.subscribers += value
        self.save()


class Subscriptions(models.Model):
    subscriber = models.ForeignKey(Channels, related_name='subscriber', on_delete=models.CASCADE)
    subscription = models.ForeignKey(Channels, related_name='subscription', on_delete=models.CASCADE)

    def __str__(self):
        return f"subscriber: {self.subscriber}, subscription: {self.subscription}"
