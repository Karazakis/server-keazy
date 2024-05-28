#!/bin/sh

# Attendere che il database sia pronto
echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Eseguire le migrazioni
python manage.py migrate

# Collezionare i file statici
python manage.py collectstatic --noinput

# Avviare Gunicorn
exec "$@"
