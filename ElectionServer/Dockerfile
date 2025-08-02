FROM python:3.13-alpine

# Обновляем pip и ставим необходимые для сборки пакеты
RUN pip install --upgrade pip \
 && apk add --no-cache \
      bash \
      postgresql-client \
      postgresql-dev \
      gcc \
      musl-dev \
      python3-dev

WORKDIR /app

COPY requirements.txt .

# Теперь psycopg2 (или любой другой пакет с C-расширениями) соберётся без ошибок
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "./entrypoint.sh"]
