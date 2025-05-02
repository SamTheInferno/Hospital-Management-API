from django.urls import path
from . import views

urlpatterns = [
    path('auth/<action>/', views.auth, name='auth'),
    path('patients/', views.AddPatient.as_view(), name='add_patient'),
    path('patients/<int:id>/', views.ModifyPatient.as_view(), name='modify_patient'),
    path('doctors/', views.AddDoctor.as_view(), name='add_doctor'),
    path('doctors/<int:id>/', views.ModifyDoctor.as_view(), name='modify_doctor'),
    path('mappings/', views.Mapping.as_view(), name='mapping'),
    path('mappings/<int:patient_id>/', views.Mapping.as_view(), name='mapping'),
]