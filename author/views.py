from typing import Any
from django.shortcuts import render, redirect, HttpResponseRedirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import  LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class UserSignUpView(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('user_login')
    form_class = forms.RegistrationForm
    success_message = "account created successfully"

class UserLoginView(LoginView):
    template_name = 'signup.html'
    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in info incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

class UserLogoutView(LogoutView):
    pass