from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Post(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    time_posted = models.DateTimeField(default=datetime.now())


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='origin_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='origin_user')
    time_posted = models.DateTimeField(default=datetime.now())


class Like(models.Model):
    liked = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_liked')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')


class Profile(models.Model):
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    