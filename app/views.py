from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def profile(request):
    return render(request,'pages/profile.html')

def editprofile(request):
    return render(request,'pages/editprofile.html')

def farm(request):
    return render(request,'pages/farm.html')

def register(request):
    return render(request,'accounts/register.html')

def loginpage(request):
    return render(request,'accounts/login.html')

def logoutuser(request):
    return redirect('login')