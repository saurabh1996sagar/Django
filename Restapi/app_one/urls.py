from django.contrib import admin
from django.urls import path
from app_one.views import CartView

urlpatterns = [
    path('shopping/',CartView.as_view()),
    path('shopping/<str:pk>',CartView.as_view()),
]