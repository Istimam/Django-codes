from typing import Any
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save(commit=True)
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'add_author.html', {'author': author_form})

def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            messages.success(request, 'Account Created Successfully')
            register_form.save(commit=True)
            return redirect('register')
    else:
        register_form = forms.RegisterForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('profile')
            else:
                messages.warning(request, 'Invalid Credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type': 'login'})

class UserLoginForm(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Login successful')
        return super().form_valid(form)        
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in Information Incorrect')
        return super().form_invalid(form)        
    def get_context_data(self, **kwargs): # form name passing from class view
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context
@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html',{'data' : data} )
@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserData(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save(commit=True)
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserData(instance = request.user)
    return render(request, 'update_profile.html', {'form': profile_form})

def pass_change(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm( request.user,data=request.POST)
        if pass_form.is_valid():
            pass_form.save()
            messages.success(request, 'Password Changed Successfully')
            update_session_auth_hash(request, pass_form.user)
            return redirect('profile')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form': pass_form})

def user_logout(request):
    logout(request)
    return redirect('login')