from django.shortcuts import render, redirect
from .models import Post, Comment, Like, Profile
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, ProfileForm
from django.http import HttpResponseRedirect

# Create your views here.
def homepage(request):
    posts = Post.objects.all().order_by('-time_posted')
    form = PostForm()
    commentForm = CommentForm()
    comments = Comment.objects.all()
    user = request.user
    profile = Profile.objects.all()
    return render(request, 'homepage.html',{'form':form,'posts':posts,'commentForm':commentForm,'comments':comments, 'profile': profile})

def profile(request):
    user = request.user
    posts = Post.objects.filter(user=user)
    form = PostForm()
    commentForm = CommentForm()
    comments = Comment.objects.all()
    user = request.user
    profile = Profile.objects.all()
    profile_form = ProfileForm()
    return render(request, 'profile.html',{'form':form,'posts':posts,'commentForm':commentForm,'comments':comments, 'profile': profile, 'profile_form': profile_form})

def profile_edit(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            profiles = Profile.objects.filter(user=request.user)
            profiles.delete()
            profile = Profile()
            profile.user = request.user
            profile.image = request.FILES['image']
            profile.save()
            return redirect('profile')
        


def post_body(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
