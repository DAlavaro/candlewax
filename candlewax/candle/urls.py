from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('info/', info, name='info'),
    path('about/', about, name='about'),
    path('delivery/', delivery, name='delivery'),
    path('reviews/', reviews, name='reviews'),
]