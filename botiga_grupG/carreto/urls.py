from django.urls import path, include
from . import views

urlpatterns = [
    #rutas de los endpoints
   # path('', views.hello_world, name='hello'),
    path('addProductosCarreto', views.add_productos_al_carreto, name='addProductosCarreto'),
    path('readProductosCarreto', views.get_productos_by_carrito, name='readProductosCarreto'),
    path('deleteProductosCarreto', views.eliminarProductoCarreto, name='deleteProductosCarreto'),

    path('', views.read_carreto, name='readCarreto'),
    path('updateCarreto/<int:pk>/update-cantidad/', views.update_carreto , name='updateCarreto')
]