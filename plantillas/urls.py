from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.plantillas_view, name='plantillas_view'),
    path('<int:pk>',views.plantilla_view,name='plantilla_view')
]