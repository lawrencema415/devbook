from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from accounts.models import UserProfile
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """do we want to CASCADE on delete?"""
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

#based on Max Goodridge's youtube tutorial Part 56
class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def befriend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    @classmethod
    def unfriend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)
