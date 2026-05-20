from django.db import migrations
from django.contrib.auth.hashers import make_password

# migration para gerar superusuário no site que está no ar
def criar_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username = 'admin').exists():
        User.objects.create(
            username = 'admin',
            email = 'roblesdocarmo@gmail.com',
            password = make_password('essenteAWU123!@#'),
            is_staff = True,
            is_superuser = True,
        )

def reverter(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username = 'admin').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_superuser, reverter),
    ]