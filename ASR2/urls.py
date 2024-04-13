from django.contrib import admin
from django.urls import path
from ASR2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.deployment, name='deployment'),
]