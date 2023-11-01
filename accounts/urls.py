from django.urls import path #First Import for path/locations of urls
from . import views #Second import for views modles in the site

urlpatterns = [
    
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]