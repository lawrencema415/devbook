from django.shortcuts import render, redirect
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
from .forms import PostForm
# Create your views here.
def homepage(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('homepage', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'homepage.html',{'form':form})
