#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py createsuperuser

gunicorn --pythonpath src config.wsgi:application --bind 0.0.0.0:8000