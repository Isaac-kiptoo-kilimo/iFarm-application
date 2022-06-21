from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from app.decorators import unauthenticated_user
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms import ProfileForm
from django.db.models import Q
from django.views.generic import TemplateView, ListView


def index(request):
    return render(request,'pages/index.html')

def profile(request):
    return render(request,'pages/profile.html')

def editprofile(request):
    return render(request,'pages/editprofile.html')

def farm(request):
    return render(request,'pages/farm.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1==password2:   
                new_user,create = User.objects.get_or_create(first_name=first_name,last_name=last_name,username=username,email=email)
                if create:
                    try:
                        validate_password(password1)
                        new_user.password = make_password(password1)
                        new_user.profile.first_name=first_name
                        new_user.profile.last_name=last_name
                        new_user.profile.username=username
                        new_user.profile.email_user=email
                        new_user.profile.save()
                        new_user.save()
                        return redirect('login')
                    except ValidationError as e:
                        messages.error(request,'Password error {e} ')
        else:
            messages.error(request,"Passwords do not match")
            return redirect('/register')    

    return render(request,'accounts/register.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
       
        user=authenticate(username=username,password=password)
        print(user)
        
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'User with this credentials not found')
    return render(request,'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')