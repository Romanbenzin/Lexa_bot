from telebot import types
from telegram_bot.pass_bot import users
from telegram_bot.helpers import list_formatter

class Handler:
    def __init__(self, bot):
        self.bot = bot

    def handle_start(self, message):
        markup = types.ReplyKeyboardMarkup()
        itembtn1 = types.KeyboardButton('/help')
        markup.add(itembtn1)
        self.bot.send_message(
            message.chat.id,
            "Привет, я бот ЛЕХА. Напиши /help, чтобы узнать мои команды."
        )

    def handle_help(self, message):
        markup = types.ReplyKeyboardMarkup()
        dota = types.KeyboardButton('/dota')
        cs = types.KeyboardButton('/cs')
        markup.add(dota, cs)
        self.bot.send_message(message.chat.id, "Мои команды:"
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
                                          "\n12. /db - База данных"
                         )  # , reply_markup=markup)

    def handle_voting_dota(self, message):
        self.bot.send_message(message.chat.id, list_formatter(users))
        question = 'Опрос на крутую игру два. Посмотри во сколько создан опрос и выбери вариант ответа.'
        options = ['да', '10 мин', '20 мин', '30 мин', '60 мин', '83 дня', 'я б лучше в каэс два']
        self.bot.send_poll(message.chat.id, question, options, is_anonymous=False)

    def handle_voting_cs(self, message):
        self.bot.send_message(message.chat.id, list_formatter(users))
        question = 'Опрос на крутую стрелялку два. Посмотри во сколько создан опрос и выбери вариант ответа.'
        options = ['да', '10 мин', '20 мин', '30 мин', '60 мин', '83 дня', 'я б лучше в дотан два']
        self.bot.send_poll(message.chat.id, question, options, is_anonymous=False)

