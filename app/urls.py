from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.frontend, name='frontend'),
    path('backend', views.backend, name='backend'),

    path('add-patient/', views.add_patient, name='add_patient'),
    path('delete-patient/<str:patient_id>/', views.delete_patient, name='delete_patient'),
    path('patient/<str:patient_id>/', views.patient, name='patient'),
    path('edit-patient/', views.edit_patient, name='edit_patient'),
]
