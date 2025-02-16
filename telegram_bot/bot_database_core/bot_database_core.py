import re
from data_base.data_base_actions import (user_add, user_delete, game_add, game_get, get_all_user_names, get_all_user_names_without_yana)
from telegram_bot.helpers import list_formatter

class DbHandler:
    def __init__(self, bot):
        self.bot = bot

    def handle_get_users_without_yana(self, message):
        self.bot.send_message(message.chat.id, list_formatter(get_all_user_names_without_yana()))

    def handle_get_users(self, message):
        self.bot.send_message(message.chat.id, list_formatter(get_all_user_names()))

    def handle_user_add(self, message):
        # Разбиваем сообщение на части
        parts = message.text.split()
        # Проверяем, что сообщение содержит достаточно аргументов
        if len(parts) < 2:
            self.bot.reply_to(message,
                         "Используйте: /db_user_add <имя_пользователя> <sucker (опционально, по умолчанию True)>")
            return
        # Извлекаем имя пользователя
        user_name = parts[1]
        # Извлекаем значение sucker (если указано)
        sucker = True  # Значение по умолчанию
        if len(parts) >= 3:
            sucker = parts[2].lower() == "true"  # Преобразуем строку в булево значение
        # Добавляем пользователя в базу данных
        result = user_add(user_name, sucker)
        # Отправляем результат пользователю
        self.bot.reply_to(message, result)

        self.bot.send_message(message.chat.id, list_formatter(get_all_uses_name()))
        self.bot.send_message(message.chat.id, list_formatter(get_all_uses_name_without_yana()))

    def handle_user_delete(self, message):
        # Разбиваем сообщение на части
        parts = message.text.split()
        # Проверяем, что сообщение содержит достаточно аргументов
        if len(parts) < 2:
            self.bot.reply_to(message, "Используйте: /db_user_delete <имя_пользователя>")
            return
        # Извлекаем имя пользователя
        user_name = parts[1]
        # Удаляем пользователя из базы данных
        result = user_delete(user_name)
        # Отправляем результат пользователю
        self.bot.reply_to(message, result)

        self.bot.send_message(message.chat.id, list_formatter(get_all_uses_name()))
        self.bot.send_message(message.chat.id, list_formatter(get_all_uses_name_without_yana()))

    def handle_game_add(self, message):
        parts = message.text.split(maxsplit=2)  # Ожидаем три части: команда, user_ids, url_game

        # Проверяем, что сообщение содержит достаточно аргументов
        if len(parts) < 3:
            self.bot.reply_to(message, "Используйте: /db_game_add <user_ids> <url_game>")
            return

        user_ids = parts[1].strip()  # Убираем лишние пробелы
        url_game = parts[2].strip()

        # Проверяем, что user_ids корректны
        if not re.match(r'^\d+(,\d+)*$', user_ids):
            self.bot.reply_to(message, "Ошибка: user_ids должны быть в формате 1,2,4")
            return

        # Проверяем, что URL корректный
        if not re.match(r'^https://store\.steampowered\.com/app/\d+/.+', url_game):
            self.bot.reply_to(message, "Ошибка: Некорректный Steam URL.")
            return

        user_ids_list = [uid.strip() for uid in user_ids.split(",")]
        if any(not uid.isdigit() for uid in user_ids_list):
            self.bot.reply_to(message, "Ошибка: Все user_ids должны быть числами.")
            return

        user_ids_clean = ",".join(user_ids_list)

        # Добавляем игру в базу данных
        result = game_add(user_ids_clean, url_game)

        self.bot.reply_to(message, result)

    def handle_game_get(self, message):
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            self.bot.reply_to(message, "Используйте: /db_get_game <имя_пользователя>")
            return

        user_name = parts[1]
        games = game_get(user_name)

        if isinstance(games, list):
            if games:
                response = "Список покупок пользователя:\n"
                for index, game in enumerate(games, start=1):
                    game_link = game[0]  # Берем ссылку на игру
                    purchase_date = str(game[1])  # Преобразуем дату в строку

                    # Извлекаем название игры из URL
                    match = re.search(r'/app/\d+/([^/]+)/', game_link)
                    game_name = match.group(1).replace('_', ' ') if match else "Unknown Game"

                    # Функция для экранирования спецсимволов в MarkdownV2
                    def escape_md(text):
                        return re.sub(r'([\_\*\[\]\(\)\~\`\>\#\+\-\=\|\{\}\.\!])', r'\\\1', text)

                    game_name_safe = escape_md(game_name)
                    game_link_safe = escape_md(game_link)
                    purchase_date_safe = escape_md(purchase_date)

                    response += f"{index}\\. [{game_name_safe}]({game_link_safe}) \\({purchase_date_safe}\\)\n"
            else:
                response = "У пользователя нет покупок."
        else:
            response = games  # Ошибка запроса

        self.bot.send_message(message.chat.id, response, parse_mode="MarkdownV2")

#    def handle_game_delete(self, message):
