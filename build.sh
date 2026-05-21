#!/usr/bin/env bash
set -e

echo "=== Instalando dependências ==="
pip install -r requirements.txt

echo "=== Listando pasta static/ ==="
ls -la static/ || echo "Pasta static/ não encontrada!"
ls -la static/css/ || echo "Pasta css/ não encontrada!"
ls -la static/img/ || echo "Pasta img/ não encontrada!"

echo "=== Migrações ==="
python manage.py migrate

echo "=== Coletando estáticos ==="
python manage.py collectstatic --noinput

echo "=== Verificando staticfiles ==="
ls -la staticfiles/ || echo "Pasta staticfiles não criada!"

echo "=== Criando superuser ==="
python manage.py createsuperuser --noinput || true

echo "=== Build concluído ==="