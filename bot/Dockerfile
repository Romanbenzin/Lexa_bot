FROM python:3.9-slim

# Установка зависимостей системы
RUN apt-get update -y && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY bot/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем весь код бота (вместе с __init__.py)
COPY bot /app/bot

# Устанавливаем PYTHONPATH, чтобы 'bot' распознавался как пакет
ENV PYTHONPATH="/app"

# Запуск через модуль
CMD ["python", "-m", "bot.telegram_bot.bot"]
