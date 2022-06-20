from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('accounts/register/',views.register,name='register'),
    path('accounts/login/',views.loginpage,name='login'),
    # path('farm/',views.farm,name='farm'),
]