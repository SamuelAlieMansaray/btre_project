from django.urls import path #First Import for path/locations of urls
from . import views #Second import for views modles in the site

urlpatterns = [
    
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]