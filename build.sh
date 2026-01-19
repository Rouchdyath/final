#!/usr/bin/env bash
set -o errexit

cd backend
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Créer un superutilisateur automatiquement si il n'existe pas
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'Motdepasse123!')" | python manage.py shell