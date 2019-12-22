from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    image = models.ImageField(upload_to='blog/images/', height_field=None, width_field=None, max_length=100, blank=True)
    pinned = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    content = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content