#!/usr/bin/env bash
set -e
echo "=== Instalando dependências ==="
pip install -r requirements.txt

echo "=== Rodando migrações ==="
python manage.py migrate

echo "=== Coletando estáticos ==="
python manage.py collectstatic --noinput -v 3

echo "=== Verificando staticfiles ==="
ls -la staticfiles/
ls -la staticfiles/css/ || echo "Pasta CSS não encontrada"

echo "=== Criando superuser ==="
python manage.py createsuperuser --noinput || true

echo "=== Build concluído ==="