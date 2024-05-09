from django.urls import path
from . import views

urlpatterns = [

    path('pagaCarreto/<int:pk>/', views.paga_carreto, name='pagaCarreto'),
]