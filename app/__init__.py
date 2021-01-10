import os
import logging
from playhouse.db_url import connect
from peewee import DatabaseProxy
from dotenv import dotenv_values
from flask import Flask
from plugins.ngrok_listener import NgrokListener
from plugins.telebot_wrapper import TelebotWrapper


bot = TelebotWrapper()
ngrok_listener = NgrokListener()
db = DatabaseProxy()


def create_app():
    app = Flask(__name__)
    config = {
        **dotenv_values(".env"),
        **os.environ
    }
    app.config.from_mapping(config)
    gunicorn_error_logger = logging.getLogger('gunicorn.error')
    telebot_logger = logging.getLogger('TeleBot')
    telebot_logger.setLevel('DEBUG')

    app.logger.handlers.extend(gunicorn_error_logger.handlers)
    app.logger.handlers.extend(telebot_logger.handlers)
    app.logger.setLevel('DEBUG')

    ngrok_listener.init_app(app)

    db_object = connect(app.config.get('DATABASE_URL'))
    db.initialize(db_object)

    bot.init_app(app=app, token=app.config.get('TELEGRAM_TOKEN'), parse_mode='HTML', threaded=False)

    return app


from app import models
from app import bot_handlers
