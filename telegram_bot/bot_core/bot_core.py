import random
import requests

from data_base.data_base_actions import get_all_user_names_without_yana
from team_speak.team_speak_server import status_server
from deepseek.requests_to_deepseek import api_request
from telebot import types
from telegram_bot.bot_database_core.bot_database_core import DbHandler
from telegram_bot.static_data.urls import izhevsk_url
from telegram_bot.static_data.vote import bot_command_help, dota_question, dota_options, cs_options, cs_question, \
    pivo_list, bot_command_start, bot_command_leha


class Handler:
    def __init__(self, bot):
        self.bot = bot
        self.data_base_handler = DbHandler(bot)

    def handle_start(self, message):
        markup = types.ReplyKeyboardMarkup()
        itembtn1 = types.KeyboardButton('/help')
        markup.add(itembtn1)
        self.bot.send_message(
            message.chat.id,
            bot_command_start
        )

    def handle_help(self, message):
        markup = types.ReplyKeyboardMarkup()
        dota = types.KeyboardButton('/dota')
        cs = types.KeyboardButton('/cs')
        markup.add(dota, cs)
        self.bot.send_message(
            message.chat.id,
            bot_command_help
        )  # , reply_markup=markup)

    def handle_voting_dota(self, message):
        self.data_base_handler.handle_get_users(message)
        self.bot.send_poll(message.chat.id, dota_question, dota_options, is_anonymous=False)

    def handle_voting_cs(self, message):
        self.data_base_handler.handle_get_users(message)
        self.bot.send_poll(message.chat.id, cs_question, cs_options, is_anonymous=False)

    def handle_leha(self, message):
        self.bot.send_message(message.chat.id, bot_command_leha)

    def handle_pivo(self, message):
        random_answer = random.choice(pivo_list)
        self.bot.send_message(message.chat.id, f"Если ты думал попить пивка, сходить покакать или поиграть в компик, "
                                          f"то я скажу тебе: \n{random_answer}")

    def handle_sosal(self, message):
        users_list = get_all_user_names_without_yana()
        user = random.choice(users_list)
        self.bot.send_message(message.chat.id, f"{user} сосал?")

    def handle_uebishche(self, message):
        users_list = get_all_user_names_without_yana()
        user = random.choice(users_list)
        self.bot.send_message(message.chat.id, f"Уебище это: {user}")

    def handle_weather(self, message):
        response = requests.get(izhevsk_url)
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
