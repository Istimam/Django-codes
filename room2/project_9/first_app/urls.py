from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name= 'homepage'),
    path('set_session/', views.set_session, name= 'homepage'),
    path('get_session/', views.get_session, name= 'homepage' ),
    path('del_session/', views.delete_session, name= 'homepage' ),
    path('get/', views.get_cookie, name= 'homepage'),
    path('del/', views.delete_cookie, name= 'homepage'),
]