from telebot import TeleBot
from flask import Flask
import inspect


class TelebotWrapper(TeleBot):
    __allowed = inspect.getfullargspec(TeleBot.__init__).args

    def __init__(self, app: Flask = None):

        self.app = app
        if app is not None:
            self.init_app(app)

        super(TelebotWrapper, self).__init__(app)

    def init_app(self, app: Flask = None, **kwargs):
        if app is not None:
            self.app = app

        for k, v in kwargs.items():
            assert (k in self.__class__.__allowed),\
                f'{k} is not a supported argument for __init__ method in TeleBot class'
            setattr(self, k, v)

    def setup_webhook(self):
        wh = self.get_webhook_info()
        tg_webhook_url = config.get('HOST_URL') + '/' + config.get('TELEGRAM_TOKEN')
        if not wh.url == tg_webhook_url:
            self.remove_webhook()
            self.set_webhook(url=tg_webhook_url)