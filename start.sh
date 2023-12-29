#!/bin/bash
source .env
python3 wait_for_postgres.py
python3 manage.py migrate
python3 manage.py init_user
python3 manage.py runserver $ALLOWED_HOSTS:$DJANGO_PORTS