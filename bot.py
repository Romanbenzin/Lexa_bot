import requests

import pass_bot
import random

from telebot import types

from pass_bot import users_without_yana
from deepseek.requests_to_deepseek import api_request
from team_speak.team_speak_server import status_server

bot = pass_bot.bot

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('/help')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Привет, я бот ЛЕХА. Напиши /help, чтобы узнать мои команды.")#, reply_markup=markup)

@bot.message_handler(commands=['bot_help'])
def bot_help(message):
    markup = types.ReplyKeyboardMarkup()
    dota = types.KeyboardButton('/dota')
    cs = types.KeyboardButton('/cs')
    markup.add(dota, cs)
    bot.send_message(message.chat.id, "Мои команды:"
                                      "\n1. /start  -   запускает бота"
                                      "\n2. /dota   -   Опросник по доте (только для крутых)"
                                      "\n3. /cs     -   Опросник по контре (только для крутых)"
                                      "\n4. /lexa   -   Поздороваться с ЛЕХОЙ (ЗОМБИ)"
                                      "\n5. /pivo   -   Рандомайзер, думаешь попить пивка или нет? - запускай"
                                      "\n6. /sosal  -   Узнать у рандомного участника сосал ли он."
                                      "\n7. /uebishche  -   Узнать кто уебище"
                                      "\n8. /weather_izh - Узнать погоду в ижевске"
                                      "\n9. /roll-n - Кинуть ролл. n - от 1 до n"
                                      "\n10. /i - запрос в deepseek"
                                      "\n11. /teamspeak_status - статус teamspeak сервера"
                     )#, reply_markup=markup)


@bot.message_handler(commands=['dota'])
def dota(message):
    bot.send_message(message.chat.id, pass_bot.users)
    question = 'Опрос на крутую игру два. Посмотри во сколько создан опрос и выбери вариант ответа.'
    options = ['да', '10 мин', '20 мин', '30 мин', '60 мин', '83 дня', 'я б лучше в каэс два']
    poll = bot.send_poll(message.chat.id, question, options, is_anonymous=False)
    print(poll)

@bot.message_handler(commands=['cs'])
def cs(message):
    bot.send_message(message.chat.id, pass_bot.users)
    question = 'Опрос на крутую стрелялку два. Посмотри во сколько создан опрос и выбери вариант ответа.'
    options = ['да', '10 мин', '20 мин', '30 мин', '60 мин', '83 дня', 'я б лучше в дотан два']
    poll = bot.send_poll(message.chat.id, question, options, is_anonymous=False)
    print(poll)

@bot.message_handler(commands=['lexa'])
def lexa(message):
    bot.send_message(message.chat.id, "Привет, вы вызвали ЛЕХУ-ЗОМБИ")

@bot.message_handler(commands=['pivo'])
def pivo(message):
    choise_list = ['Да, сделай это!', 'Нет, не делай этого, не надо дядя']
    random_answer = random.choice(choise_list)
    bot.send_message(message.chat.id, f"Если ты думал попить пивка, сходить покакать или поиграть в компик, "
                                      f"то я скажу тебе: \n{random_answer}")

@bot.message_handler(commands=['sosal'])
def sosal(message):
    user = random.choice(users_without_yana)
    bot.send_message(message.chat.id, f"{user} сосал?")

@bot.message_handler(commands=['uebishche'])
def sosal(message):
    user = random.choice(users_without_yana)
    bot.send_message(message.chat.id, f"Уебище это: {user}")

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