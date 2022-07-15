from django.urls import path
from . import views
from.views import *

urlpatterns= [
    path('patients/',PatientListView.as_view() , name='patients'),
    path('patients/add',PatientCreateView.as_view(), name='ajouter_patient'),
    path('patients/<int:pk>/update',PatientUpdateView.as_view(), name='modifier_patient'),
    path('patients/<int:pk>/delete',PatientDeleteView.as_view(), name='suprimer_patient'),
    path('rdv/<str:pk>',PatientDetailView.as_view(),name='RDV'),
    path('rdv/<str:pk>/ajouter',RDVCreateView.as_view(), name='ajouter_rdv'),
]