from data_base.data_base_actions import get_all_uses_name, get_all_uses_name_without_yana, user_add, user_delete
from telegram_bot.helpers import list_formatter

class DbHandler:
    def __init__(self, bot):
        self.bot = bot

    def handle_get_users(self, message):
        self.bot.send_message(message.chat.id, list_formatter(get_all_uses_name()))
        self.bot.send_message(message.chat.id, list_formatter(get_all_uses_name_without_yana()))

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
