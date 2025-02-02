import psycopg2
from psycopg2 import Error
from telegram_bot.pass_bot import DB_CONFIG

def connect_to_db():
    """Функция для подключения к базе данных."""
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(**DB_CONFIG)
        print("Подключение к базе данных успешно установлено.")
        return connection
    except Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None

def close_connection(connection):
    """Функция для закрытия соединения с базой данных."""
    if connection:
        connection.close()
        print("Соединение с базой данных закрыто.")
