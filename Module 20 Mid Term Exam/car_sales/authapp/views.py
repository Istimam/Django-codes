from django.shortcuts import render, redirect,  get_object_or_404
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
class RegisterFormView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'You have successfully registered')
        return response

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context
    
class CustomLoginView(LoginView):
    template_name = 'signup.html'
    success_url = reverse_lazy('profile')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        user_name = form.cleaned_data.get('username')
        user_pass = form.cleaned_data.get('password')
        user = authenticate(username=user_name, password=user_pass)
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, 'Login successful')
            return super().form_valid(form)
        else:
            messages.add_message(self.request, messages.WARNING, 'Login unsuccessful')
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.WARNING, 'Login information is invalid')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
def Logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have been logged out successfully.')
        return HttpResponseRedirect(reverse_lazy('login'))