from django.urls import path
from . import views

urlpatterns = [
    path('auth/<action>/', views.auth, name='auth'),
]