#!/bin/bash

# create root admin user
python manage.py createsuperuser --noinput

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files (optional, mainly for production)
python manage.py collectstatic --noinput

# Start the server
python manage.py runserver 0.0.0.0:8000
