from django.urls import path
from . import views

urlpatterns = [
    path('auth/<action>/', views.auth, name='auth'),
    path('patients/', views.add_patient.as_view(), name='add_patient'),
]