#!/bin/bash
set -e

echo "Ожидание запуска Postgres"

until pg_isready -h "$POSTGRES_HOST" -d "$POSTGRES_DB" -U "$POSTGRES_USER"; do
  sleep 5
done

echo "Postgres запущена. Выполнение миграций..."
python manage.py makemigrations
python manage.py migrate

if [ "$TEST" = "1" ]; then
  echo "Запуск тестов..."
  python manage.py test
  exit 0
fi

WORKERS=$(( $(nproc) * 2 + 1 ))
echo "Запуск Gunicorn с $WORKERS воркерами..."

exec gunicorn ElectionServer.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers "$WORKERS" \
  --timeout 60 \
  --access-logfile - \
  --error-logfile - \
  --log-level info