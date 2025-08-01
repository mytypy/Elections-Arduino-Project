set -e

echo "Ожидание запуска MySQL..."

until mysqladmin ping -h "$MYSQL_HOST" -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" --silent; do
echo "MySQL недоступна — ожидаем"
sleep 5
done

echo "MySQL запущена. Выполнение миграций..."
python manage.py migrate

echo "Запуск API..."
exec uvicorn main:app --host 0.0.0.0 --port 8000