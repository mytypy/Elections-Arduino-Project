FROM python:3.13-alpine

RUN apk add --no-cache \
    bash \
    mariadb-client

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "./entrypoint.sh"]