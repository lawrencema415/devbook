from django import forms
from .models import Post, Comment, Like
# bounding form to post model
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('body',)