from django.urls import path, include
from . import views

urlpatterns = [
    # path('register/', views.Register_Form, name='register'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # path('logout/', views.Logoutview, name='logout'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    # path('login/', views.login_form, name= 'login'),
    
]