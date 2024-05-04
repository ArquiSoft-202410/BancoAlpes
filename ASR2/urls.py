from django.urls import path
from ASR2 import views

urlpatterns = [
    path('', views.deployment, name='deployment'),
]