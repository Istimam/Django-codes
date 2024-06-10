from django.urls import path, include
from . import views
urlpatterns = [
    path('register/',views.register, name='register'),
    # path('login/',views.user_login, name='login'),
    path('login/',views.UserLoginForm.as_view(), name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('profile/edit/',views.edit_profile, name='edit_profile'),
    path('profile/edit/passChange/',views.pass_change, name='pass_change'),
]