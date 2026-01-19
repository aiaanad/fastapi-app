# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Установка системных зависимостей для mysql-connector
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Копирование зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода
COPY src/ .

# Запуск приложения
CMD ["python", "app.py"]