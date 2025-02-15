import random
import requests

from team_speak.team_speak_server import status_server
from deepseek.requests_to_deepseek import api_request
from telebot import types
from telegram_bot.pass_bot import users, users_without_yana
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

    def handle_leha(self, message):
        self.bot.send_message(message.chat.id, "Привет, вы вызвали ЛЕХУ-ЗОМБИ")

    def handle_pivo(self, message):
        choise_list = ['Да, сделай это!', 'Нет, не делай этого, не надо дядя']
        random_answer = random.choice(choise_list)
        self.bot.send_message(message.chat.id, f"Если ты думал попить пивка, сходить покакать или поиграть в компик, "
                                          f"то я скажу тебе: \n{random_answer}")

    def handle_sosal(self, message):
        user = random.choice(users_without_yana)
        self.bot.send_message(message.chat.id, f"{user} сосал?")

    def handle_uebishche(self, message):
        user = random.choice(users_without_yana)
        self.bot.send_message(message.chat.id, f"Уебище это: {user}")

    def handle_weather(self, message):
        response = requests.get(
            'https://api.open-meteo.com/v1/forecast?latitude=56.8498&longitude=53.2045&hourly=temperature_2m&forecast_days=1')
        list_of_temperature = response.json()['hourly']['temperature_2m']
        self.bot.send_message(message.chat.id, f"Минимальная температура сегодня в Ижевске : {min(list_of_temperature)}")
        self.bot.send_message(message.chat.id, f"Максимальная температура сегодня в Ижевске : {max(list_of_temperature)}")

    def handle_ii(self, message):
        try:
            # Лог для отладки
            print(f"Получено сообщение: {message.text}")

            # Извлекаем текст запроса из команды
            command_parts = message.text.split(maxsplit=1)  # Разделяем команду и текст запроса
            if len(command_parts) < 2:
                self.bot.send_message(message.chat.id, "Пожалуйста, укажите текст запроса после команды /i")
                return

            user_request = command_parts[1].strip()  # Текст запроса
            if not user_request:
                self.bot.send_message(message.chat.id, "Запрос не может быть пустым.")
                return

            # Формируем запрос к DeepSeek
            response = api_request(user_request)

            # Обработка ответа
            if response.status_code == 200:
                answer = response.json()["choices"][0]["message"]["content"]
                self.bot.send_message(message.chat.id, answer)
            else:
                self.bot.send_message(message.chat.id, f"Ошибка при запросе к API: {response.status_code}")

            print("Запрос:", message.text)
            print("Ответ:", response.status_code, response.text)

        except Exception as e:
            # Логируем ошибку
            print(f"Ошибка: {e}")
            self.bot.send_message(message.chat.id, "Произошла ошибка при обработке запроса.")

    def handle_roll(self, message):
        try:
            # Лог для отладки
            print(f"Получено сообщение: {message.text}")

            # Извлекаем значение n из команды
            command_parts = message.text.split('-')
            if len(command_parts) != 2 or not command_parts[1].isdigit():
                self.bot.send_message(message.chat.id,
                                 "Пожалуйста, используйте команду в формате /roll-n, где n - максимальное число.")
                return

            n = int(command_parts[1])
            if n < 1:
                self.bot.send_message(message.chat.id, "Число n должно быть больше 0.")
                return

            # Генерируем случайное число
            number = random.randint(1, n)
            self.bot.send_message(message.chat.id, f"Вы выбросили число: {number}")
        except Exception as e:
            print(f"Ошибка: {e}")  # Логирование ошибки
            self.bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

    def handle_just_roll(self, message):
        self.bot.send_message(message.chat.id,
                         "Пожалуйста, используйте команду в формате /roll-n, где n - максимальное число.")

    def handle_team_speak_status(self, message):
        response = status_server()
        self.bot.send_message(message.chat.id, f"Статус сервера teamspeak: {response}")

    def handle_message_from_user(self, message):
        user = message.from_user
        chat_id = message.chat.id
        try:
            if message.text.lower() == 'привет леха!':
                self.bot.send_message(chat_id, f"Привет, @{user.username}!")
            else:
                pass
        except:
            pass
