#!/usr/bin/env sh

# sleep for 30 seconds to let MySQL container start & create database
 sleep 30

cd /app/web
export DJANGO_SECRET=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

cat >.env <<EOL
DJANGO_SECRET=${DJANGO_SECRET}
web_db_name=django
web_db_user=admin
web_db_pass=123321
EOL
./manage.py makemigrations
./manage.py migrate
./manage.py shell < seeds.py
./manage.py runserver 0.0.0.0:8000