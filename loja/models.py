from django.db import models
from django.contrib.auth.models import User

# ===================
# MODEL 1: CATEGORIA
# ===================
class Categoria(models.Model):
    # Essa tabela organiza os produtos em categorias
    # Ex: Velas, sabonetes, sprays, difusores

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    origem = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nome

# =================
# MODEL 2: PRODUTO
# =================
class Produto(models.Model):
    
    # Tabela principal - cada produto da loja
    
    nome = models.CharField(max_length = 200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits = 10, decimal_places = 2)
    estoque = models.IntegerField(default = 0)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank = True, null = True)
    data_cadastro = models.DateTimeField(auto_now_add = True)
    disponivel = models.BooleanField(default = True)
    
    # Campos específicos para produtos aromáticos
    aroma = models.CharField(max_length = 100, blank = True, null = True)
    peso_ml = models.CharField(max_length = 50, blank = True, null = True)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        return self.nome


# =================
# MODEL 3: CLIENTE
# =================
class Cliente(models.Model):
    
    #  Cadastro dos clientes da loja
   
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    nome = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    telefone = models.CharField(max_length = 20, blank = True, null = True)
    endereco = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.nome

# ================ 
# MODEL 4: PEDIDO
# ================
class Pedido(models.Model):
    
    # Registro de cada venda realizada
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('preparando', 'Preparando'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default='pendente')
    total = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    observacao = models.TextField(blank = True, null = True)
    
    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.nome}'

# ========================
# MODEL 5: ITEM DO PEDIDO
# ========================
class ItemPedido(models.Model):
   
    # Produtos específicos dentro de cada pedido
    
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete = models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits = 10, decimal_places = 2)
    
    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome}'
    
    @property
    def subtotal(self):
        """Calcula o subtotal do item (quantidade × preço)"""
        return self.quantidade * self.preco_unitario