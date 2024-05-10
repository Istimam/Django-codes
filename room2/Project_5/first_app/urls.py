from django.urls import path
from .import views

# app_name = 'first_app'

urlpatterns = [
    path('',views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('form/', views.submit_form, name= 'form'),
    path('django_form/', views.PasswordValidation, name= 'django_form'),
]