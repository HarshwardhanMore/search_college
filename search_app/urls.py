from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.start),
    path('home',views.home),
    path('search_colleges',views.search_colleges,name="search_colleges"),
]
