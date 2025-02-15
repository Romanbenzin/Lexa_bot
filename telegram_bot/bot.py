import requests
import pass_bot
import random
import re
from telebot import types
from deepseek.requests_to_deepseek import api_request
from team_speak.team_speak_server import status_server
from data_base.data_base_actions import game_get
from telegram_bot.bot_core.bot_core import Handler
from telegram_bot.bot_database_core.bot_database_core import DbHandler

bot = pass_bot.bot
handler = Handler(bot)
data_base_handler = DbHandler(bot)

@bot.message_handler(commands=['start'])
def start(message):
    handler.handle_start(message)

@bot.message_handler(commands=['bot_help'])
def bot_help(message):
    handler.handle_help(message)

@bot.message_handler(commands=['dota'])
def dota(message):
    handler.handle_voting_dota(message)

@bot.message_handler(commands=['cs'])
def cs(message):
    handler.handle_voting_cs(message)

@bot.message_handler(commands=['lexa'])
def lexa(message):
    handler.handle_leha(message)

@bot.message_handler(commands=['pivo'])
def pivo(message):
    handler.handle_pivo(message)

@bot.message_handler(commands=['sosal'])
def sosal(message):
    handler.handle_sosal(message)

@bot.message_handler(commands=['uebishche'])
def uebishche(message):
    handler.handle_uebishche(message)

@bot.message_handler(commands=['db_user_get'])
def db_user_get(message):
    data_base_handler.handle_get_users(message)

@bot.message_handler(commands=['db_user_add'])
def db_user_add(message):
    data_base_handler.handle_user_add(message)

@bot.message_handler(commands=['db_user_delete'])
def db_user_delete(message):
    data_base_handler.handle_user_delete(message)

@bot.message_handler(commands=['db_game_add'])
def game_add(message):
    data_base_handler.handle_game_add(message)

@bot.message_handler(commands=['db_game_get'])
def db_game_get(message):
    data_base_handler.handle_game_get(message)

#@bot.message_handler(commands=['db_game_delete'])
#def db_game_delete(message):
#    data_base_handler.handle_game_delete(message)

@bot.message_handler(commands=['weather_izh'])
def weather_izh(message):
    response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=56.8498&longitude=53.2045&hourly=temperature_2m&forecast_days=1')
    list_of_temperature = response.json()['hourly']['temperature_2m']
    bot.send_message(message.chat.id, f"Минимальная температура сегодня в Ижевске : {min(list_of_temperature)}")
    bot.send_message(message.chat.id, f"Максимальная температура сегодня в Ижевске : {max(list_of_temperature)}")

@bot.message_handler(func=lambda message: message.text and message.text.startswith('/i'))
def request_to_ii(message):
    try:
        # Лог для отладки
        print(f"Получено сообщение: {message.text}")

        # Извлекаем текст запроса из команды
        command_parts = message.text.split(maxsplit=1)  # Разделяем команду и текст запроса
        if len(command_parts) < 2:
            bot.send_message(message.chat.id, "Пожалуйста, укажите текст запроса после команды /i")
            return

        user_request = command_parts[1].strip()  # Текст запроса
        if not user_request:
            bot.send_message(message.chat.id, "Запрос не может быть пустым.")
            return

        # Формируем запрос к DeepSeek
        response = api_request(user_request)

        # Обработка ответа
        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]["content"]
            bot.send_message(message.chat.id, answer)
        else:
            bot.send_message(message.chat.id, f"Ошибка при запросе к API: {response.status_code}")

        print("Запрос:", message.text)
        print("Ответ:", response.status_code, response.text)

    except Exception as e:
        # Логируем ошибку
        print(f"Ошибка: {e}")
        bot.send_message(message.chat.id, "Произошла ошибка при обработке запроса.")

@bot.message_handler(func=lambda message: message.text and message.text.startswith('/roll-'))
def roll_with_arg(message):
    try:
        # Лог для отладки
        print(f"Получено сообщение: {message.text}")

        # Извлекаем значение n из команды
        command_parts = message.text.split('-')
        if len(command_parts) != 2 or not command_parts[1].isdigit():
            bot.send_message(message.chat.id,
                             "Пожалуйста, используйте команду в формате /roll-n, где n - максимальное число.")
            return

        n = int(command_parts[1])
        if n < 1:
            bot.send_message(message.chat.id, "Число n должно быть больше 0.")
            return

        # Генерируем случайное число
        number = random.randint(1, n)
        bot.send_message(message.chat.id, f"Вы выбросили число: {number}")
    except Exception as e:
        print(f"Ошибка: {e}")  # Логирование ошибки
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

@bot.message_handler(commands=['roll'])
def roll(message):
    bot.send_message(message.chat.id, "Пожалуйста, используйте команду в формате /roll-n, где n - максимальное число.")

@bot.message_handler(commands=['teamspeak_status'])
def teamspeak_status(message):
    response = status_server()
    bot.send_message(message.chat.id, f"Статус сервера teamspeak: {response}")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user = message.from_user
    chat_id = message.chat.id
    try:
        if message.text.lower() == 'привет леха!':
            bot.send_message(chat_id, f"Привет, @{user.username}!")
        else:
            pass
    except:
        pass

bot.set_my_commands([
    types.BotCommand("start",   "Запустить бота"),
    types.BotCommand("bot_help",    "Показать список команд"),
    types.BotCommand("dota",    "Опросник по доте"),
    types.BotCommand("cs",      "Опросник по контер стрике"),
    types.BotCommand("lexa",    "Поздороваться с ЛЕХА ЗОМБИ"),
    types.BotCommand("pivo",    "Рандомайзер, думаешь попить пивка или нет? - запускай"),
    types.BotCommand("sosal",   "Узнать у рандомного участника сосал ли он"),
    types.BotCommand("uebishche",   "Узнать кто уебище"),
    types.BotCommand("weather_izh",   "Узнать погоду в ижевске"),
    types.BotCommand("roll",   "Кинуть ролл"),
    types.BotCommand("i",   "Запрос к deepseek"),
    types.BotCommand("teamspeak_status",   "Узнать статус сервера ts")
])

bot.polling()