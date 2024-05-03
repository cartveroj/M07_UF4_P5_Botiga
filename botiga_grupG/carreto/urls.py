from django.urls import path, include
from . import views

urlpatterns = [
    #rutas de los endpoints
    path('', views.hello_world, name='hello'),
    path('addCarreto', views.add_carreto, name='addCarreto'),
    path('readCarreto/', views.read_carreto, name='readCarreto')
]