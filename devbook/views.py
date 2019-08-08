from django.shortcuts import render, redirect
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    form = PostForm()
    commentForm = CommentForm()
    comments = Comment.objects.all()
    return render(request, 'homepage.html',{'form':form,'posts':posts,'commentForm':commentForm,'comments':comments})

def post_body(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('homepage')
    return redirect('homepage')

def post_comment(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('homepage')
    else:
        form = CommentForm()
        return redirect('homepage')
