from django.shortcuts import render
from .models import Produto, Categoria
# create your views here
def home(request):
    produtos = Produto.objects.filter(disponivel=True).order_by('-data_cadastro')[:8]
    categorias = Categoria.objects.all()
    
    contexto = {
        'produtos': produtos,
        'categorias': categorias,
    }
    return render(request, 'loja/home.html', contexto)