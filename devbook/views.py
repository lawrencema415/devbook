from django.shortcuts import render, redirect
from .models import Post, Comment, Like, Profile, Friend, Message
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, ProfileForm, LikeForm, MessageForm, UserProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def homepage(request):
    posts = Post.objects.all().order_by('-time_posted')
    form = PostForm()
    commentForm = CommentForm()
    comments = Comment.objects.all()
    likeForm = LikeForm()
    user = request.user
    profile = Profile.objects.all()
    likes = Like.objects.all()
    return render(request, 'homepage.html',{'form':form,'posts':posts,'commentForm':commentForm,'comments':comments, 'profile': profile, 'likes':likes,'likeForm':likeForm})

def friends(request):
    posts = Post.objects.all()
    form = PostForm()
    commentForm = CommentForm()
    comments = Comment.objects.all()
    users = User.objects.all()
    user = request.user
    profile = Profile.objects.all()
    return render(request, 'homepage.html',{'form':form,'posts':posts,'commentForm':commentForm,'comments':comments, 'profile': profile, 'users':users})

@login_required
def profile(request):
    user = request.user
    posts = Post.objects.filter(user=user)
    form = PostForm()
    commentForm = CommentForm()
    comments = Comment.objects.all()
    profile = Profile.objects.get(user=user)
    profile_form = ProfileForm()
    return render(request, 'profile.html',{'form':form,'posts':posts,'commentForm':commentForm,'comments':comments, 'profile': profile, 'profile_form': profile_form})

def profile_edit(request):
    form = ProfileForm(request.POST)
    print(request.FILES.get('image', False))
    if request.FILES.get('image', False):
        if form.is_valid():
            if request.method == 'POST':
                profiles = Profile.objects.filter(user=request.user)
                profiles.delete()
                profile = Profile()
                profile.user = request.user
                profile.image = request.FILES['image']
                profile.save()
                return redirect('profile')
    else:
        return redirect('profile')

@login_required
def post_body(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def post_delete(request, pk):
    Post.objects.get(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('homepage')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form, 'header': f'Edit Post'})

@login_required
def post_comment(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def comment_edit(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('homepage')
    else:
        form = PostForm(instance=comment)
    return render(request, 'comment_form.html', {'form': form, 'header': f'Edit Comment'})

def delete_comment(request,pk):
    Comment.objects.get(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def like_post(request,pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        form = LikeForm(request.POST)
        like = form.save(commit=False)
        like.post = post
        like.user = request.user
        if Like.objects.filter(user=like.user,post=post).exists():
            Like.objects.filter(user=like.user,post=post).delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            like.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def user_prof(request,pk):
    profile = Profile.objects.get(id=pk)
    profile_form = ProfileForm()
    return render(request, 'userprofile.html',{"profile":profile,"profile_form":profile_form })

@login_required
def user_profile_edit(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user_form.html', {'form': form, 'header': f'Edit Profile'})

def search(request):
    name = request.POST['name']
    user = User.objects.filter(first_name__icontains=name)
    if name is not "":
        profile = []
        for user in user:
            if Profile.objects.get(user=user):
                profile.append(Profile.objects.get(user=user))
    else:
        profile = Profile.objects.all()
    profile_form = ProfileForm()
    return render(request, 'search.html',{"profile":profile})

@login_required
def get_mail(request,pk):
    user = User.objects.get(id=pk)
    messages = Message.objects.filter(receiver=user)
    return render(request, 'inbox.html',{"messages":messages})

def mail(request,pk):
    messageForm = MessageForm()
    profile = Profile.objects.filter(id=pk)
    return render(request, 'send_mail.html',{"profile":profile,"messageForm":messageForm})

@login_required
def send_mail(request,pk):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            user = request.user
            user = User.objects.get(id=user.pk)
            profile = Profile.objects.get(id=pk)
            receiver = User.objects.get(id=profile.user.pk)
            message = form.save(commit=False)
            message.sender = user
            message.receiver = receiver
            message.save()
            profile = Profile.objects.get(id=pk)
            profile_form = ProfileForm()
            return render(request, 'userprofile.html',{"profile":profile,"profile_form":profile_form })
