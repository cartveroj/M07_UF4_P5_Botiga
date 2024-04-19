from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    #rutas de los endpoints
    # path('', views.hello_world, name='hello'),
     path('addCarreto/', views.add_carreto, name='addCarreto'),
     path('', views.read_carreto, name='readCarreto')
 ]