#!/usr/bin/env bash
set -e

echo "=== Instalando dependências ==="
pip install -r requirements.txt

echo "=== Migrações ==="
python manage.py migrate

echo "=== Coletando estáticos ==="
python manage.py collectstatic --noinput

echo "=== Criando superuser ==="
python manage.py createsuperuser --noinput || true

echo "=== Build concluído ==="