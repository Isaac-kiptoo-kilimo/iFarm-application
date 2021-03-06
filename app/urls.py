from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns=[
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editProfile,name='editprofile'),
    path('post/',views.post,name='post'),
    path('accounts/register/',views.register,name='register'),
    # path('accounts/farmer/register/',views.register_farmer,name='farmer_register'),
    path('accounts/login/',views.loginpage,name='login'),
    # path('accounts/officer/register/',views.register_officer,name='officer_register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('officer/', views.officer, name='officer'),
    path('farmer/', views.farmer, name='farmer'),
    path("addquestion", views.addquestion, name="addquestion"),
    path("single/<int:post_id>/", views.single, name="single"),
    path("question/", views.question,name="question"),
    path("detail/<int:id>/", views.question_detail, name="detail"),
    path("delete/<int:post_id>/", views.delete, name="delete"),
    path('accounts/logout/',views.logoutUser,name='logout'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    # path('neighbor/',views.neighbor,name='neighbor'),
    # path('hood/',views.hood,name='hood'),
    # path("single/<int:neighbourhood_id>/", views.single_hood, name="single"),
    # path("join/<int:id>/", views.join_hood, name="join"),
    # path("leave/<int:id>/", views.leave_hood, name="leave"),
    # path('addbusiness/<int:neighbourhood_id>/',views.addbusiness,name='addbusiness'),
    # # path('farm/',views.farm,name='farm'),
]