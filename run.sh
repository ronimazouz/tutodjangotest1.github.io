#!/bin/bash

export DJANGO_SETTINGS_MODULE=tuto.settings_dev;
python3 manage.py makemigrations;
python3 manage.py migrate;
python3 manage.py collectstatic;
python3 manage.py runserver;
