#!/bin/sh
python manage.py migrate --settings=config.settings.prod
python manage.py makemigrations --settings=config.settings.prod
python manage.py migrate --settings=config.settings.prod
python manage.py runserver --settings=config.settings.prod 0.0.0.0:8080
