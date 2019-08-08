from django import forms
from .models import Post, Comment, Like
# bounding form to post model
class PostForm(forms.ModelForm):
    body = forms.CharField()
    class Meta:
        model = Post
        fields = ('body',)
