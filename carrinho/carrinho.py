from decimal import Decimal
from loja.models import Produto

class Carrinho:
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get('carrinho')
        if not carrinho:
            carrinho = self.session['carrinho'] = {}
        self.carrinho = carrinho

    def adicionar(self, produto_id, quantidade=1):
        produto_id = str(produto_id)
        if produto_id not in self.carrinho:
            produto = Produto.objects.get(id=produto_id)
            self.carrinho[produto_id] = {
                'nome': produto.nome,
                'preco': str(produto.preco),
                'quantidade': quantidade,
            }
        else:
            self.carrinho[produto_id]['quantidade'] += quantidade
        self.salvar()

    def remover(self, produto_id):
        produto_id = str(produto_id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.salvar()

    def salvar(self):
        self.session.modified = True

    def __len__(self):
        return sum(item['quantidade'] for item in self.carrinho.values())

    def __iter__(self):
        for produto_id, item in self.carrinho.items():
            item['produto_id'] = produto_id
            item['preco'] = Decimal(item['preco'])
            item['subtotal'] = item['preco'] * item['quantidade']
            yield item

    def total(self):
        return sum(Decimal(item['preco']) * item['quantidade'] for item in self.carrinho.values())

    def limpar(self):
        del self.session['carrinho']
        self.session.modified = True