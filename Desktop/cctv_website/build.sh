#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); u=User.objects.get(username='admin'); u.set_password('Admin@123'); u.save()" | python manage.py shell

python manage.py collectstatic --noinput