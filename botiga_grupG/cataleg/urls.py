from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello_world, name='index'),
    path('crearProd/', views.afegir_producte, name='crearProducte'),
    path('updateProd/<str:pk>/', views.actualitza_producte, name='actualitzaProducte'),
    path('productes/', views.veure_productes, name= 'productes'),
    path('producte/<str:pk>/', views.veure_producte, name='producte'),
    path('deleteProd/<str:pk>/', views.elimina_producte, name='eliminaProducte')
]