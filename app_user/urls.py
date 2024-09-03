from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'app_user'

urlpatterns = [
    path('login/', views.UserLogin.as_view(),name='login'),
    path('signup/email_signup/',views.UserRegistration,name='email_signup'),
    path('api/user/', views.UserDetailView.as_view(), name='user-detail'),

]