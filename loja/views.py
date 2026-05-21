
from django.shortcuts import render
from .models import Produto, Categoria
from django.http import JsonResponse
import cloudinary
import cloudinary.uploader
# create your views here
# rota para a página principal - Home
def home(request):
    produtos = Produto.objects.filter(disponivel = True).order_by('-data_cadastro')[:8]
    categorias = Categoria.objects.all()
    
    contexto = {
        'produtos': produtos,
        'categorias': categorias,
    }
    return render(request, 'loja/home.html', contexto)

# rota para a página de Sobre
def sobre(request):
    return render(request, 'loja/sobre.html')

# rota para a página de Produtos
def produtos(request):
    produtos = Produto.objects.filter(disponivel = True).order_by('nome')
    categorias = Categoria.objects.all()
    
    contexto = {
        'produtos': produtos,
        'categorias': categorias
    }
    return render(request, 'loja/produtos.html', contexto)

# teste de upload de imagens para o Cloudinary
def test_upload(request):
    try:
        result = cloudinary.uploader.upload(
            "https://res.cloudinary.com/demo/image/upload/sample.jpg",
            public_id="teste_essente"
        )
        return JsonResponse({'sucesso': True, 'url': result['secure_url']})
    except Exception as e:
        return JsonResponse({'erro': str(e)})