from data_base.data_base_actions import get_all_uses_name, get_all_uses_name_without_yana
from telegram_bot.helpers import list_formatter

class DbHandler:
    def __init__(self, bot):
        self.bot = bot

    def handle_get_users(self, message):
        self.bot.send_message(message.chat.id, list_formatter(get_all_uses_name()))
        self.bot.send_message(message.chat.id, list_formatter(get_all_uses_name_without_yana()))
