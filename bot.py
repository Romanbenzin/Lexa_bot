import pass_bot
import telebot
from telebot import types
#@bebrazin_bot
bot = pass_bot.bot

@bot.message_handler(commands=['start'])
def start(message):
    #markup = types.ReplyKeyboardMarkup()
    #itembtn1 = types.KeyboardButton('/help')
    #markup.add(itembtn1)
    bot.send_message(message.chat.id, "Привет, я бот ЛЕХА. Напиши /help, чтобы узнать мои команды.")#, reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    #markup = types.ReplyKeyboardMarkup()
    #itembtn1 = types.KeyboardButton('/dota - запускает крутой опросник для игры в доту 2')
    #itembtn2 = types.KeyboardButton('/lexa - можно круто призвать леху зомби')
    #itembtn3 = types.KeyboardButton('/tatar - можно круто предложить татарину отсосать')
    #markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Мои команды:"
                                      "\n1. /start  -   запускает бота"
                                      "\n2. /dota   -   Опросник по доте (только для крутых)"
                                      "\n3. /lexa   -   Поздороваться с ЛЕХОЙ (ЗОМБИ)"
                                      "\n4. /tatar  -   Предложить татарину отсосать пенис")#, reply_markup=markup)

@bot.message_handler(commands=['dota'])
def dota(message):
    bot.send_message(message.chat.id, "@rshchetnikov, @hqdicq, @DaniilPletnev, @Ya_umit, @tim_utt")
    question = 'Опрос на крутую игру два'
    options = ['да', '10 мин', 'часик', 'не буду в компик (я сережа)']
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