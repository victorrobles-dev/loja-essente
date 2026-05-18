from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrinho_resumo, name='carrinho_resumo'),
    path('adicionar/<int:produto_id>/', views.carrinho_adicionar, name='carrinho_adicionar'),
    path('remover/<int:produto_id>/', views.carrinho_remover, name='carrinho_remover'),
    path('whatsapp/', views.whatsapp_mensagem, name='whatsapp_mensagem'),
]