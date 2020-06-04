from django.contrib import admin
from django.urls import path,include
from api import views
urlpatterns = [
    path('get_data/', views.get_data),
]