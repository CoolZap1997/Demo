from django.contrib import admin
from django.urls import path
from .views import index, sayHello

urlpatterns = [
    path('', index),
    path('<str:name>', sayHello)
]
