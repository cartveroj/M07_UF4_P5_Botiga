from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello_world, name='index'),
    path('crearProd', views.afegir_producte, name='crearProducte')
]