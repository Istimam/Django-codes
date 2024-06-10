from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', views.signUp, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.pass_change, name='passchange'),
    path('change_password2/', views.pass_change2, name='passchange2'),
]