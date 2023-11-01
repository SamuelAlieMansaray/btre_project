from django.urls import path #First Import for path/locations of urls
from . import views #Second import for views modles in the site

urlpatterns = [
    
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
