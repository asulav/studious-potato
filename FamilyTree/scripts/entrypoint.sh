#!/bin/bash
set -e

source .env
python manage.py install_labels
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000