import config_bot
from telebot import types
from telegram_bot.bot_core.bot_core import Handler
from telegram_bot.bot_database_core.bot_database_core import DbHandler

bot = config_bot.bot
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

@bot.message_handler(commands=['animal'])
def animal(message):
    handler.animal(message)

@bot.message_handler(commands=['weather_izh'])
def weather_izh(message):
    handler.handle_weather(message)

@bot.message_handler(func=lambda message: message.text and message.text.startswith('/i'))
def request_to_ii(message):
    handler.handle_ii(message)

@bot.message_handler(func=lambda message: message.text and message.text.startswith('/roll-'))
def roll_with_arg(message):
    handler.handle_roll(message)

@bot.message_handler(commands=['roll'])
def roll(message):
    handler.handle_just_roll(message)

@bot.message_handler(commands=['teamspeak_status'])
def teamspeak_status(message):
    handler.handle_team_speak_status(message)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    handler.handle_message_from_user(message)

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
    types.BotCommand("teamspeak_status",   "Узнать статус сервера ts"),
    types.BotCommand("animal",   "Узнать о случайном животном")
])

bot.polling(none_stop=True)