from django.urls import path
from . import views

urlpatterns= [
    path('login/', views.login),
    path('patients/', views.patients , name='patients'),
    path('ajouter patient/', views.ajouter_patient, name='ajouter_patient'),
    path('rdv/<str:pk>', views.rdv, name='RDV'),
]