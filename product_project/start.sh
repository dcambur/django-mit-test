#!/bin/bash

sleep 15
# Run database migrations
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --noinput
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
