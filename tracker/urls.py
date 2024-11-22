from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('log-meal/', views.log_meal, name='log_meal'),
    path('log-workout/', views.log_workout, name='log_workout'),
    path('log-water/', views.log_water, name='log_water'),
]
