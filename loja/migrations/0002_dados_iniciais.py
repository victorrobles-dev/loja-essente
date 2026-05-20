from django.db import migrations

def criar_dados_iniciais(apps, schema_editor):
    Categoria = apps.get_model('loja', 'Categoria')
    Produto = apps.get_model('loja', 'Produto')
    
    # Categorias
    velas = Categoria.objects.create(
        nome='Velas', 
        descricao='Velas artesanais aromáticas para todos os ambientes',
        origem='Produção artesanal brasileira'
    )
    sabonetes = Categoria.objects.create(
        nome='Sabonetes', 
        descricao='Sabonetes naturais para pele macia e perfumada',
        origem='Produção artesanal brasileira'
    )
    difusores = Categoria.objects.create(
        nome='Difusores', 
        descricao='Difusores aromáticos para ambientes',
        origem='Produção artesanal brasileira'
    )
    kits = Categoria.objects.create(
        nome='Kits', 
        descricao='Kits especiais para presentear',
        origem='Produção artesanal brasileira'
    )
    
    # Produtos
    Produto.objects.create(
        nome='Vela de Pêssego com Damasco',
        descricao='Vela artesanal com óleo essencial de pêssego e damasco. Aroma suave e relaxante, ideal para momentos de tranquilidade.',
        preco=29.90, estoque=50, categoria=velas, aroma='Pêssego com Damasco', peso_ml='200g', disponivel=True
    )
    Produto.objects.create(
        nome='Vela de Baunilha',
        descricao='Vela aromática de baunilha com notas adocicadas. Perfeita para criar um ambiente acolhedor.',
        preco=34.90, estoque=30, categoria=velas, aroma='Baunilha', peso_ml='200g', disponivel=True
    )
    Produto.objects.create(
        nome='Sabonete de Erva Doce',
        descricao='Sabonete artesanal com extrato natural de erva doce. Limpeza suave e perfume delicado.',
        preco=15.90, estoque=40, categoria=sabonetes, aroma='Erva Doce', peso_ml='100g', disponivel=True
    )
    Produto.objects.create(
        nome='Sabonete de Alecrim',
        descricao='Sabonete natural de alecrim, revigorante e refrescante para o dia a dia.',
        preco=15.90, estoque=35, categoria=sabonetes, aroma='Alecrim', peso_ml='100g', disponivel=True
    )
    Produto.objects.create(
        nome='Difusor de Canela',
        descricao='Difusor aromático de canela para ambientes. Aroma quente e convidativo.',
        preco=24.90, estoque=25, categoria=difusores, aroma='Canela', peso_ml='150ml', disponivel=True
    )
    Produto.objects.create(
        nome='Difusor de Eucalipto',
        descricao='Difusor de eucalipto refrescante. Ideal para purificar e energizar ambientes.',
        preco=24.90, estoque=20, categoria=difusores, aroma='Eucalipto', peso_ml='150ml', disponivel=True
    )
    Produto.objects.create(
        nome='Kit Relax',
        descricao='Kit especial com Vela de Pêssego e Damasco + Sabonete de Erva Doce + Difusor de Eucalipto.',
        preco=59.90, estoque=15, categoria=kits, aroma='Pêssego e Damasco, Erva Doce e Eucalipto', peso_ml='Conjunto', disponivel=True
    )
    Produto.objects.create(
        nome='Kit Aconchego',
        descricao='Kit completo: Vela de Baunilha + Sabonete de Alecrim + Difusor de Canela.',
        preco=64.90, estoque=10, categoria=kits, aroma='Baunilha, Alecrim e Canela', peso_ml='Conjunto', disponivel=True
    )

def reverter_dados(apps, schema_editor):
    Categoria = apps.get_model('loja', 'Categoria')
    Produto = apps.get_model('loja', 'Produto')
    Produto.objects.all().delete()
    Categoria.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('loja', '0004_alter_categoria_origem'),
    ]
    
    operations = [
        migrations.RunPython(criar_dados_iniciais, reverter_dados),
    ]