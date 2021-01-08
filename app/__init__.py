import os
import telebot
import logging
from pyngrok import ngrok
from dotenv import dotenv_values
from flask import Flask
from plugins.ngrok_listener import NgrokListener

config = {
    **dotenv_values(".env"),
    **os.environ
}

bot = telebot.TeleBot(token=config.get('TELEGRAM_TOKEN'), parse_mode='HTML', threaded=False)
ngrok_listener = NgrokListener()


def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = config.get('DATABASE_URL')
    gunicorn_error_logger = logging.getLogger('gunicorn.error')
    telebot_logger = logging.getLogger('TeleBot')
    telebot_logger.setLevel('DEBUG')

    app.logger.handlers.extend(gunicorn_error_logger.handlers)
    app.logger.handlers.extend(telebot_logger.handlers)

    app.logger.setLevel('DEBUG')

    ngrok_listener.init_app(app)

    wh = bot.get_webhook_info()
    tg_webhook_url = config.get('HOST_URL') + '/' + config.get('TELEGRAM_TOKEN')
    # print(f'wh is: {wh.url} and tg_webhook_url is {tg_webhook_url}')
    if not wh.url == tg_webhook_url:
        bot.remove_webhook()
        bot.set_webhook(url=tg_webhook_url)
    # print('QIWI WEBHOOK ENABLED')

    return app
