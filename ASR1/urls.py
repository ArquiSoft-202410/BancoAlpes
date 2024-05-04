from django.urls import path
from ASR1 import views

urlpatterns = [
    path('', views.form, name='request'),
]