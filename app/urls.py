from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.frontend, name='frontend'),
    path('backend', views.backend, name='backend'),

    path('add-patient/', views.add_patient, name='add_patient'),
]
