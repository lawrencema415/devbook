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
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # check if the passwords match
        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username is already taken.'})
        # check if user exists with that email
            else:
                if User.objects.filter(email=email).exists():
                        return render(request, 'register.html', {'error': 'Email already exists. Please Log in.'})
        # if everything is okay Create a User
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)   
                    user.save()
                    return redirect('homepage')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})
    # else
    else:
        # send form
        return render(request, 'register.html')
    
def login(request):
    # if POST 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # GET form info
        # authenticate user
        user = auth.authenticate(username=username, password=password)
        print("I am in login")
        # make sure a user exists
        if user is not None:
            # login
            auth.login(request, user)
            print("test, did I actually log in???")
            # redirect
            return redirect('homepage')
        # else return not found
        else:
            print("I failed to login")
            return render(request, 'register.html', {'error': 'Invalid Credentials'})
        
    # else send form
    else:
        return render(request, 'register.html')
    
def logout(request):
    auth.logout(request);
    return redirect('signup')
