from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.UserSignUpView.as_view(), name='user_signup'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('', views.LogoutView.as_view(), name='user_logout'),
]