from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Categoria, Produto, Cliente, Pedido, ItemPedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Colunas que aparecem na listagem

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'categoria', 'disponivel')
    list_filter = ('categoria', 'disponivel')  # Filtros laterais
    search_fields = ('nome', 'descricao')  # Campo de busca

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email')

class ItemPedidoInline(admin.TabularInline):  # Permite editar itens dentro do pedido
    model = ItemPedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data_pedido', 'status', 'total')
    list_filter = ('status', 'data_pedido')
    inlines = [ItemPedidoInline]  # Itens do pedido aparecem juntos