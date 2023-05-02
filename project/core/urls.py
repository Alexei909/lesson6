from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('addpage/', add_page, name='add_page'),
    path('contact/', contact, name='contact')
    
]