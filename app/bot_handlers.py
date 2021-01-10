from app import bot
from flask import current_app
from app.models import User


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.reply_to(message, 'Hey there! Try texting anything :)')
        user = User.get_or_create(chat_id=message.chat.id,
                                  id=message.from_user.id,
                                  first_name=message.from_user.first_name,
                                  last_name=message.from_user.last_name,
                                  username=message.from_user.username)
        user = user[0]
    except Exception as e:
        current_app.logger.error(f'Error occured in send_welcome handler: {e}')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    try:
        bot.reply_to(message, message.text)
    except Exception as e:
        current_app.logger.error(f'Error occured in echo_message handler: {e}')
