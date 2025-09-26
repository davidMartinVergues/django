#!/bin/bash

# # Wait for postgres
# echo "Waiting for postgres..."
# until nc -z postgres 5432; do
#   sleep 0.1
# done
# echo "PostgreSQL started"

# # Run migrations
# echo "Running migrations..."
# python manage.py migrate --noinput

if [ "$DJANGO_DEBUG" = "true" ]
then
    echo "Running Django in debug mode"
    if [ "$DJANGO_DEBUG_SHELL" = "true" ]
    then
        echo "Starting Django shell with debugpy on port 5679"
        python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5679 --wait-for-client manage.py shell
    else
        echo "Starting Django server with debugpy on port 5678"
        python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 --wait-for-client manage.py runserver 0.0.0.0:8000
    fi
else
    echo "Running Django in production mode"
    python manage.py runserver 0.0.0.0:8000
fi