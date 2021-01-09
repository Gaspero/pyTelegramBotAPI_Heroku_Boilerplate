from app import bot


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hey there! Try texting anything :)')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)