import telebot
bot = telebot.TeleBot('7385255905:AAHYbZdHtqUMqiaiX-ZnWOoTNgCJrZGRREg')

@bot.message_handler(content_types=['text', 'document', 'audio'])
def handle_text(message):
    if "LEXA DOTA" in message.text.upper():
        question = 'в дотку пидоры?'
        options = ['да', 'пизда', 'леха', 'нет, я гей']
        poll = bot.send_poll(message.chat.id, question, options, is_anonymous=False)
        print(poll)
    elif "LEXA" in message.text.upper():
        bot.send_message(message.chat.id, "Привет, вы вызвали LEXY зомби")
    elif "TATAR" in message.text.upper():
        bot.send_message(message.chat.id, "@hqdicq хотел бы мне отсосать? (я леха)")
    else:
        pass


bot.polling(none_stop=True, interval=0)