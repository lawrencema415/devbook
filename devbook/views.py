from django.shortcuts import render, redirect
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')