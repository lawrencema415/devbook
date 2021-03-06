from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image
# Create your models here.
class Post(models.Model):
    body = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.body

    def like_count(self):
        return len(Like.objects.filter(post=self.pk))




class Comment(models.Model):
    body = models.TextField(default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.body


class Like(models.Model):
    liked = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_liked')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """do we want to CASCADE on delete?"""
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    image = models.ImageField(upload_to = 'profile_image', blank=True, default="profile_image/default.jpg")
    bio = models.CharField(max_length=200,default='')
    location = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=30,default='')

    def __str__(self):
        return self.user.first_name

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    topic = models.CharField(max_length=100,default="")
    message = models.TextField(default="")
    time_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.topic
