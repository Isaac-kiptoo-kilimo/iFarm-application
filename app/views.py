from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.decorators import unauthenticated_user
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms import ProfileForm
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# @login_required(login_url='login')
def index(request):
    posts=Post.objects.all()
    return render(request,'pages/index.html',{'posts':posts})

@login_required(login_url='login')
def profile(request):
    user=User.objects.all()
    return render(request,'pages/profile.html',{'users':user})

@login_required(login_url='login')
def question(request):
    user=User.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        question=Question.objects.filter(question_title__icontains=q).order_by('-id')
    else:
        question=Question.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(question, 1)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request,'pages/question.html',{'users':user,'questions':questions})
   
@login_required(login_url='login')
def addquestion(request):
    if request.method=='POST':
        question_title=request.POST.get('question_title')
        question=request.POST.get('question')
        question=Question(question_title=question_title,question=question,user=request.user)
        question.save_question()
        return redirect('question')
    return render(request,'pages/addquestion.html')

@login_required(login_url='login')
def question_detail(request,id):
    question=Question.objects.get(pk=id)
    tags=question.tags.split(',')
    answer=Answer.objects.get(question=question)
    context={
        'tags':tags,
        'question':question,
        'answer':answer
    }
    return render(request ,'pages/detail.html',context)


@login_required(login_url='login')
def post(request):
    if request.method=='POST':
        photo=request.FILES.get('photo')
        title=request.POST.get('title')
        description=request.POST.get('description')
        price=request.POST.get('price')
        shop=request.POST.get('shop')
        category=request.POST.get('category')
        location=request.POST.get('location')
        posts=Post(post_img=photo,title=title,description=description,user=request.user,price=price,shop=shop,category=category,location=location)
        posts.save_post()
        print('new post is ',posts)
        return redirect('index')
    return render(request,'pages/addpost.html')

@login_required(login_url='login')
def single(request,post_id):
    post = Post.objects.get(id=post_id)
    cxt={
        'post':post
    }
    return render(request,'pages/single.html',cxt)

@login_required(login_url='login')
def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('post')


@login_required(login_url='login')
def editProfile(request):
    profiles= Profile.objects.get(user=request.user)
   
    if request.method == 'POST':
       
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            
            prof_form.save()
            return redirect('profile')
            
            
    else:
        # user_form = UpdateUserForm(instance=request.user)
        prof_form = ProfileForm(instance=request.user.profile)
             
    context={
        # 'user_form': user_form,
        'prof_form': prof_form,
        'profiles': profiles
          
        }
    return render(request,'pages/editprofile.html',context)

def farm(request):
    return render(request,'pages/farm.html')

@unauthenticated_user
def register(request):
    return render(request,'accounts/register/register.html')


@unauthenticated_user
def register_farmer(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        # farmer= Farmer.objects.get_or_create(request.user.farmer)
        # farmer.save_farmer()
        # print('farmer',farmer)
        if password1==password2:  
                new_user,create = User.objects.get_or_create(first_name=first_name,last_name=last_name,username=username,email=email)
                if create:
                    try:
                        validate_password(password1)
                        new_user.password = make_password(password1)
                        new_user.is_farmer=True
                        new_user.profile.first_name=first_name
                        new_user.profile.last_name=last_name
                        new_user.profile.username=username
                        new_user.profile.email_user=email
                        new_user.profile.save()
                        print('profile',new_user)
                        new_user.save()
                        print('general',new_user)
                        # new_user.save_farmer()
                        # print('farmer',new_user)
                        messages.success(request,'Account has been created successfully')
                        return redirect('login')
                    except ValidationError as e:
                        messages.error(request,'Password error {e} ')
        else:
            messages.error(request,"Passwords do not match")
            return redirect('/register_farmer')    

    return render(request,'accounts/register/registerfarmer.html',{'messages':messages})

@unauthenticated_user  
def register_officer(request):
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
                        messages.success(request,'Account has been created successfully')
                        return redirect('login')
                    except ValidationError as e:
                        messages.error(request,'Password error {e} ')
        else:
            messages.error(request,"Passwords do not match")
            return redirect('/register_officer')    

    return render(request,'accounts/register/registerofficer.html',{'messages':messages})

@unauthenticated_user
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
    return render(request,'accounts/login/login.html')





# @login_required(login_url='login')
# def neighbor(request):
#     if request.method=='POST':
#         photo=request.FILES.get('photo')
#         neighbourhood_name=request.POST.get('neighbourhood_name')
#         location=request.POST.get('location')
#         Occupants_Count=request.POST.get('Occupants_Count')
#         health_helpline=request.POST.get('health_helpline')
#         police_helpline=request.POST.get('police_helpline')
#         description=request.POST.get('description')
#         neighbourhoods=NeighbourHood(hood_img=photo,neighbourhood_name=neighbourhood_name,health_helpline=health_helpline,police_helpline=police_helpline,Occupants_Count=Occupants_Count,location=location,description=description,user=request.user)
#         neighbourhoods.save_neighbourhood()
#         print('new neighbour is ',neighbourhoods)
#         return redirect('hood')
#     return render(request,'pages/neighbor.html')

# def single_hood(request,neighbourhood_id):
#     businesses = Business.get_hood_business(neighbourhood_id)
#     biznas = Business.objects.filter(id=neighbourhood_id)
#     neighbourhood= NeighbourHood.objects.get(id=neighbourhood_id)
#     cxt={
#         'neighbourhood':neighbourhood,
#         'businesses':businesses,
#         'biznas':biznas
#     }
#     return render(request,'pages/single.html',cxt)

# @login_required(login_url='login')
# def hood(request):
#     neighbourhoods=NeighbourHood.objects.all()
#     return render(request,'pages/view_hood.html',{'neighbourhoods':neighbourhoods})

# @login_required(login_url='login')
# def view_post(request,post_id):
#     post = Post.objects.get(id=post_id)
#     cxt={
#         'post':post
#     }
#     return render(request,'pages/view_post.html',cxt)


# def join_hood(request,id):
#     neighbourhood=NeighbourHood.objects.get(id=id)
#     user=request.user
#     user.profile.neighbourhood=neighbourhood
#     user.profile.save()
#     return redirect('hood')

# def leave_hood(request,id):
#     hood=get_object_or_404(NeighbourHood,id=id)
#     request.user.profile.neighbourhood=None
#     request.user.profile.save()
#     return redirect('hood')


# @login_required(login_url='login')
# def addbusiness(request,neighbourhood_id):
#     # business=Business.objects.filter(id=neighbourhood_id)
#     if request.method=='POST':
#         photo=request.FILES.get('photo')
#         business_name=request.POST.get('business_name')
#         business_email=request.POST.get('business_email')
#         contact=request.POST.get('contact')
#         business=Business(business_logo=photo,business_name=business_name,business_email=business_email,contact=contact,user=request.user,neighbourhood_id=NeighbourHood.objects.get(id=neighbourhood_id))
#         business.save_business()
#         print('new business is ',business)
#         return redirect('single',neighbourhood_id)
#     return render(request,'pages/addbusiness.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')



class SearchResultsView(ListView):
    model = Post
    template_name = "pages/search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("query")
        object_list = Post.objects.filter(
            Q(shop__icontains=query)
        )
        return object_list
