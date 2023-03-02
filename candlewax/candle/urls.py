from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('info/', info, name='info'),
    path('about/', about),
    path('delivery/', delivery),
    path('reviews/<slug:rev>', reviews),
]