from django.db import models
from Channels.models import Channels
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User


class VideoTags(models.Model):
    value = models.TextField(max_length=20)


def videos_upload_path(instance, filename):
    return 'videos/user_{0}/{1}'.format(instance.publisher.id, filename)


def previews_upload_path(instance, filename):
    return 'previews/user_{0}/{1}'.format(instance.publisher.id, filename)


class Videos(models.Model):
    publisher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.TextField(max_length=64)
    description = models.TextField(max_length=500, default='n/n')
    # duration = models.IntegerField(default=0)
    pub_date = models.DateTimeField("publication date", default=timezone.now())
    video_path = models.FileField(
        upload_to=videos_upload_path,
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    preview_path = models.ImageField(
        upload_to=previews_upload_path,
        default='previews/base_preview.jpg'
    )
    views = models.BigIntegerField(default=0)
    tags = models.ManyToManyField(VideoTags, null=True)

    def get_likes(self):
        return self.reactions.filter(video_id=self.id, value=True).count()

    def get_dislikes(self):
        return self.reactions.filter(video_id=self.id, value=False).count()

    def get_comments(self):
        return self.comments.filter(video_id=self.id).order_by('-pub_date')

    def views_per_day(self):
        pass

    def likes_per_day(self):
        pass

    def dislikes_per_day(self):
        pass

    def comments_per_day(self):
        pass


class Reactions(models.Model):
    author = models.ForeignKey(
        Channels,
        on_delete=models.CASCADE,
        related_name='reactions'
    )
    video = models.ForeignKey(
        Videos,
        on_delete=models.CASCADE,
        related_name='reactions'
    )
    value = models.BooleanField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'video_id: {self.video_id}, author_id: {self.author_id}, value: {self.value}, date: {self.pub_date}'


class Comments(models.Model):
    author = models.ForeignKey(
        Channels,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    video = models.ForeignKey(
        Videos,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    value = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
