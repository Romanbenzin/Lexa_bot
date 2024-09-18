import telebot

from telebot import types
#@bebrazin_bot
bot = telebot.TeleBot('5099621872:AAE0JiQvWbn90f1vv-DXmKNMBOZ8_IEMDN0')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('/help')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Привет, я бот ЛЕХА. Нажми /help, чтобы узнать мои команды.", reply_markup=markup)

#@bot.message_handler(commands=['help'])
#def help(message):
#    markup = types.ReplyKeyboardMarkup()
#    itembtn1 = types.KeyboardButton('/dota - запускает крутой опросник для игры в доту 2')
#    itembtn2 = types.KeyboardButton('/lexa - можно круто призвать леху зомби')
#    itembtn3 = types.KeyboardButton('/tatar - можно круто предложить татарину отсосать')
#    markup.add(itembtn1, itembtn2, itembtn3)
#    bot.send_message(message.chat.id, "Мои команды:", reply_markup=markup)

@bot.message_handler(commands=['dota'])
def dota(message):
    question = 'в дотку пидоры?'
    options = ['да', 'пизда', 'леха', 'нет, я гей']
    poll = bot.send_poll(message.chat.id, question, options, is_anonymous=False)
    print(poll)

@bot.message_handler(commands=['lexa'])
def lexa(message):
    bot.send_message(message.chat.id, "Привет, вы вызвали ЛЕХУ-ЗОМБИ")

@bot.message_handler(commands=['tatar'])
def tatar(message):
    bot.send_message(message.chat.id, "@hqdicq хотел бы ЛЕХЕ отсосать? (я леха)")

bot.set_my_commands([
    types.BotCommand("start", "Запустить бота"),
    types.BotCommand("help", "Показать список команд"),
    types.BotCommand("dota", "Опросник по доте"),
    types.BotCommand("lexa", "Поздороваться с ЛЕХА ЗОМБИ"),
    types.BotCommand("tatar", "Предложить татарину отсосать лехе (мне)")
])

bot.polling()
