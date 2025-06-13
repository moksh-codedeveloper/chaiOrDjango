#!/usr/bin/env bash
pip install -r requirements.txt
pip install --upgrade pip


# Run Django setup
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
