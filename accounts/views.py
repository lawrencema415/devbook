from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    # IF POST
    if request.method == 'POST':
        # get form information
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        birthday = request.POST['birthday']
        # check if the passwords match
        if password == password2:
        # check if user exists with that email
            if User.objects.filter(email=email).exists():
                    return render(request, 'register.html', {'error': 'Email already exists. Please Log in.'})
        # if everything is okay Create a User
            else:
                    user = User.objects.create_user(password=password, email=email, first_name=first_name, last_name=last_name, birthdat=birthday)   
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})
    # else
    else:
        # send form
        return render(request, 'register.html')
    
def login(request):
    # if POST 
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # GET form info
        # authenticate user
        user = auth.authenticate(email=email, password=password)
        # make sure a user exists
        if user is not None:
            # login
            auth.login(request, user)
            # redirect
            return redirect('profile')
        # else return not found
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
        
    # else send form
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request);
    return redirect('signup')