from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('itens/', views.listar_itens, name='listar_itens'),
]
