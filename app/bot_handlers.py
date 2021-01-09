from app import bot
from flask import current_app


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.reply_to(message, 'Hey there! Try texting anything :)')
    except Exception as e:
        current_app.logger.error(f'Error occured in send_welcome handler: {e}')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    try:
        bot.reply_to(message, message.text)
    except Exception as e:
        current_app.logger.error(f'Error occured in echo_message handler: {e}')
