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
        descricao='Kits especiais para presentear alguém ou a si mesmo',
        origem='Produção artesanal brasileira'
    )
    
    # Produtos pré cadastrados
    Produto.objects.create(
        nome='Vela de Pêssego e Damasco - Tamanho M',
        descricao='Vela artesanal com óleo essencial de pêssego e damasco. Aroma suave e relaxante, ideal para momentos de tranquilidade.',
        preco=27.00, estoque=20, categoria=velas, aroma='Pêssego e Damasco', peso_ml='100g', disponivel=True, imagem = 'https://res.cloudinary.com/da2dzpbf6/image/upload/q_auto/f_auto/v1779382594/vela_M_pessego_damasco_msqtjx.jpg'
    )

    Produto.objects.create(
        nome='Vela da Sorte - Tamanho P',
        descricao='Vela aromática de baunilha com notas adocicadas. Perfeita para criar um ambiente de prosperidade.',
        preco=19.80, estoque=20, categoria=velas, aroma='Baunilha', peso_ml='50g', disponivel=True, imagem = 'https://res.cloudinary.com/da2dzpbf6/image/upload/q_auto/f_auto/v1779382594/vela_M_linha_sorte_ffpewq.jpg'
    )

    Produto.objects.create(
        nome='Sabonete de Pêssego e Damasco',
        descricao='Sabonete artesanal com extrato natural de pêssego com damasco. Limpeza suave e perfume delicado.',
        preco=12.90, estoque=15, categoria=sabonetes, aroma='Pêssego e Damasco', peso_ml='100g', disponivel=True, imagem = 'https://res.cloudinary.com/da2dzpbf6/image/upload/q_auto/f_auto/v1779382594/sabonete_barra_pessego_damasco_jlvrjr.jpg'
    )

    Produto.objects.create(
        nome='Sabonete Líquido de Pêssego e Damasco',
        descricao='Sabonete líquido natural de pêssego com damasco, revigorante e refrescante para o dia a dia.',
        preco=39.90, estoque=35, categoria=sabonetes, aroma='Pêssego e Damasco', peso_ml='250ml', disponivel=True, imagem = 'https://res.cloudinary.com/da2dzpbf6/image/upload/q_auto/f_auto/v1779382594/sabonete_liquido_pessego_damasco_j5enmn.jpg'
    )

    Produto.objects.create(
        nome='Difusor Linha Nobre',
        descricao='Difusor aromático de canela para ambientes. Aroma quente e convidativo.',
        preco=63.90, estoque=20, categoria=difusores, aroma='Canela', peso_ml='200ml', disponivel=True, imagem = 'https://res.cloudinary.com/da2dzpbf6/image/upload/q_auto/f_auto/v1779382593/difusor_canela_ynfhvk.jpg'
    )

    Produto.objects.create(
        nome='Difusor de Pêssego e Damasco',
        descricao='Difusor de pêssego com damasco com aroma aconchegante. Ideal para purificar e energizar ambientes.',
        preco=59.90, estoque=20, categoria=difusores, aroma='Pêssego e Damasco', peso_ml='200ml', disponivel=True, imagem = 'https://res.cloudinary.com/da2dzpbf6/image/upload/q_auto/f_auto/v1779382593/difusor_pessego_damasco_id2c1w.jpg'
    )

    Produto.objects.create(
        nome='Kit Relax',
        descricao='Kit especial com Vela de Pêssego e Damasco + Sabonete de Pêssego e Damasco',
        preco=38.80, estoque=8, categoria=kits, aroma='Pêssego e Damasco', peso_ml='Conjunto', disponivel=True, imagem = 'https://res.cloudinary.com/da2dzpbf6/image/upload/q_auto/f_auto/v1779382594/kit_sabonete_e_vela_nwwz1k.jpg'
    )

    Produto.objects.create(
        nome='Kit Linha Pêssego e Damasco',
        descricao='Kit completo: Vela de Pêssego e Damasco + Sabonete de Pêssego e Damasco + Sabonete líquido de Pêssego e Damasco + Difusor de Pêssego e Damasco.',
        preco=137.90, estoque=8, categoria=kits, aroma='Pêssego com Damasco', peso_ml='Conjunto', disponivel=True, imagem = 'https://res.cloudinary.com/da2dzpbf6/image/upload/q_auto/f_auto/v1779382594/kit_completo_pessego_damasco_rh4mhs.jpg'
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