import pass_bot
import random
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
                                      "\n3. /cs     -   Опросник по контре (только для крутых)"
                                      "\n4. /lexa   -   Поздороваться с ЛЕХОЙ (ЗОМБИ)"
                                      "\n5. /pivo   -   Рандомайзер, думаешь попить пивка или нет? - запускай")#, reply_markup=markup)

@bot.message_handler(commands=['dota'])
def dota(message):
    bot.send_message(message.chat.id, "@rshchetnikov, @hqdicq, @DaniilPletnev, @Ya_umit, @tim_utt")
    question = 'Опрос на крутую игру два. Посмотри во сколько создан опрос и выбери вариант ответа.'
    options = ['да', '10 мин', '20 мин', '30 мин', '60 мин', '83 дня']
    poll = bot.send_poll(message.chat.id, question, options, is_anonymous=False)
    print(poll)

@bot.message_handler(commands=['cs'])
def cs(message):
    bot.send_message(message.chat.id, "@rshchetnikov, @hqdicq, @DaniilPletnev, @Ya_umit, @tim_utt")
    question = 'Опрос на крутую стрелялку два. Посмотри во сколько создан опрос и выбери вариант ответа.'
    options = ['да', '10 мин', '20 мин', '30 мин', '60 мин', '83 дня']
    poll = bot.send_poll(message.chat.id, question, options, is_anonymous=False)
    print(poll)

@bot.message_handler(commands=['lexa'])
def lexa(message):
    bot.send_message(message.chat.id, "Привет, вы вызвали ЛЕХУ-ЗОМБИ")

@bot.message_handler(commands=['pivo'])
def pivo(message):
    choise_list = ['Да, сделай это!', 'Нет, не делай этого, не надо дядя']
    random_answer = random.choice(choise_list)
    bot.send_message(message.chat.id, f"Если ты думал попить пивка, сходить покакать или поиграть в компик, то я скажу тебе: \n{random_answer}")

bot.set_my_commands([
    types.BotCommand("start",   "Запустить бота"),
    types.BotCommand("help",    "Показать список команд"),
    types.BotCommand("dota",    "Опросник по доте"),
    types.BotCommand("cs",      "Опросник по контер стрике"),
    types.BotCommand("lexa",    "Поздороваться с ЛЕХА ЗОМБИ"),
    types.BotCommand("pivo",    "Рандомайзер, думаешь попить пивка или нет? - запускай")
])

bot.polling()