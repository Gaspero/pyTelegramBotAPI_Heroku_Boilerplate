import os
import logging
from dotenv import dotenv_values
from flask import Flask
from plugins.ngrok_listener import NgrokListener
from plugins.telebot_wrapper import TelebotWrapper

config = {
    **dotenv_values(".env"),
    **os.environ
}

bot = TelebotWrapper()
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

    bot.init_app(token=config.get('TELEGRAM_TOKEN'), parse_mode='HTML', threaded=False)


    return app
