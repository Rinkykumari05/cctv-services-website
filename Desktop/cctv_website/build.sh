#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'servizable@gmail.com', 'Admin@12345')" | python manage.py shell

python manage.py collectstatic --noinput