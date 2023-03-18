from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios_view, name='usuarios_view'),
    path('<int:pk>',views.usuario_view,name='usuario_view')
]