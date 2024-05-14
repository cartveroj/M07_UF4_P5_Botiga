from django.urls import path
from . import views

urlpatterns = [
    #Urls de solo comandas
    path('readComandes', views.read_comandas, name='readComandes'),
    path('addComandes', views.add_comanda, name='addComandes'),
    path('deleteComandes', views.delete_comanda, name='deleteComandes'),
    #Urls de carritos en comanda
    path('', views.get_carritos_by_comanda, name='readComandesCarretos'),
    path('pendientesCarritos', views.get_pendientes_carritos, name='pendientesCarritos'),
    path('historicoCarritos', views.get_historico_carritos, name='historicoCarritos'),

]