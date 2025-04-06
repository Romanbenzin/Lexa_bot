import telebot
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
# пароль от бд
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_HOST_CONTAINER = os.getenv("POSTGRES_HOST_CONTAINER")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

# ключ от тг бота
TG_KEY_PROD = os.getenv("TG_BOT_PROD")
TG_KEY_STAGE = os.getenv("TG_BOT_TEST")
# Выбрать значение в зависимости от нужной среды
bot = telebot.TeleBot(TG_KEY_STAGE)

DB_CONFIG = {
    "dbname": POSTGRES_DB,  # Имя базы данных
    "user": POSTGRES_USER,  # Имя пользователя
    "password": POSTGRES_PASSWORD,  # Пароль
    "host": POSTGRES_HOST_CONTAINER,  # Хост (обычно localhost) (host.docker.internal - чтобы смотреть в локальную базу) # POSTGRES_HOST_CONTAINER = db
    "port": POSTGRES_PORT  # Порт (по умолчанию 5432)
}
