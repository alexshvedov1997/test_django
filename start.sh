#!/bin/bash
python3 manage.py migrate
source .env
python3 manage.py init_user
python3 manage.py runserver $ALLOWED_HOSTS:$DJANGO_PORTS