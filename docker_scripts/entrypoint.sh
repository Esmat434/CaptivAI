#!/bin/sh

set -e

echo "📦 Applying database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "🧱 Collecting static files..."
python manage.py collectstatic --noinput

exec "$@"