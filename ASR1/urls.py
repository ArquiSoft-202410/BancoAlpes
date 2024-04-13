from django.contrib import admin
from django.urls import path
from ASR1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.form, name='request'),
]