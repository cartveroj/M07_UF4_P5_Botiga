from django.urls import path, include
from . import views

urlpatterns = [
    #rutas de los endpoints
   # Urls de carretos con productos
    path('addProductosCarreto/', views.add_productos_al_carreto, name='addProductosCarreto'),
    path('readProductosCarreto/', views.get_productos_by_carrito, name='readProductosCarreto'),
    path('deleteProductosCarreto/', views.eliminar_productos_carreto, name='deleteProductosCarreto'),
    path('updateProductosCarreto/', views.update_producto_carreto , name='updateProductosCarreto'),
    # Urls de carretos
    path('', views.read_carreto, name='readCarreto'),
    path('addCarreto/', views.add_carreto, name='addCarreto'),
    path('deleteCarreto/<str:pk>/', views.delete_carreto, name='deleteCarreto'),

]