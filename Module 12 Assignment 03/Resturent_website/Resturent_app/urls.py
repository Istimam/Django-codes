from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name = 'items'),
    path('aboutUs/', views.about, name = 'aboutUs'),
]