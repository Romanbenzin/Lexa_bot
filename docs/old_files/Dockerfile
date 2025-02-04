# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости проекта
COPY requirements.txt .

# Установка системных зависимостей
RUN apt-get update -y && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем переменную окружения PYTHONPATH
ENV PYTHONPATH=/app

# Команда для запуска бота
CMD ["python", "telegram_bot/bot.py"]