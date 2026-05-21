#!/usr/bin/env bash
set -e

echo "=== Instalando dependências ==="
pip install -r requirements.txt

echo "=== Migrações ==="
python manage.py migrate

echo "=== Verificando configuração de estáticos ==="
python -c "
from django.conf import settings
print('STATICFILES_DIRS:', settings.STATICFILES_DIRS)
print('STATIC_ROOT:', settings.STATIC_ROOT)
import os
for d in settings.STATICFILES_DIRS:
    print(f'Existe {d}?', os.path.exists(d))
"

echo "=== Listando pasta static/ ==="
ls -la static/ || echo "Pasta static/ não encontrada!"
ls -la static/css/ || echo "Pasta css/ não encontrada!"
ls -la static/img/ || echo "Pasta img/ não encontrada!"

echo "=== Coletando estáticos ==="
python manage.py collectstatic --noinput

echo "=== Verificando staticfiles ==="
ls -la staticfiles/ || echo "Pasta staticfiles não criada!"

echo "=== Criando superuser ==="
python manage.py createsuperuser --noinput || true

echo "=== Build concluído ==="