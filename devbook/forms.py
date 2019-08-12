from django import forms
from .models import Post, Comment, Like, Profile, Message
# bounding form to post model
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('body',)
        labels = {
        "body": ""
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            "body": ""
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)

class LikeForm(forms.ModelForm):

    class Meta:
        model = Like
        fields = ('liked',)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('topic','message')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'phone')
