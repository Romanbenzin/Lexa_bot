import requests

import pass_bot
import random
#import yandexcloud import ai

from telebot import types

from pass_bot import users_without_yana

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
    types.BotCommand("weather_izh",   "Узнать погоду в ижевске")
])

bot.polling()