#!/bin/bash
set -e

if [ "$1" = 'gunicorn' ]; then
    python3 manage.py migrate --noinput
    exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
fi

exec "$@"
