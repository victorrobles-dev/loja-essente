from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Produto
from .carrinho import Carrinho
from django.http import JsonResponse
# create your views here
def carrinho_resumo(request):
    carrinho = Carrinho(request)
    return render(request, 'carrinho/resumo.html', {'carrinho': carrinho})

def carrinho_adicionar(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id = produto_id)
    carrinho.adicionar(produto_id = produto.id, quantidade = 1)
    return redirect('carrinho_resumo')

def carrinho_remover(request, produto_id):
    carrinho = Carrinho(request)
    carrinho.remover(produto_id)
    return redirect('carrinho_resumo')

def whatsapp_mensagem(request):
    carrinho = Carrinho(request)
    
    if len(carrinho) == 0:
        return JsonResponse({'erro': 'Carrinho vazio'}, status=400)
    
    mensagem = "🌿 *Novo Pedido - Loja Essenté* 🌿\n\n"
    
    for item in carrinho:
        mensagem += f"• {item['quantidade']} x {item['nome']} - R$ {item['subtotal']:.2f}\n"
    
    mensagem += f"\n💰 *Total: R$ {carrinho.total():.2f}*\n\n"
    mensagem += "\nPor favor, confirme o seu pedido e envie seu endereço para entrega!"
    
    telefone = "5511976272285"
    url = f"https://wa.me/{telefone}?text={mensagem}"
    
    return JsonResponse({'url': url})