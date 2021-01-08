from app import config
from pyngrok import ngrok


class NgrokListener(object):

    def __init__(self, app=None):

        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if app is not None:
            self.app = app

        if config.get('ENVIRONMENT') == 'DEVELOPMENT':
            self.app.logger.debug(f'connecting to ngrok')
            ngrok.kill()
            http_tunnel = ngrok.connect(bind_tls=True, addr=config.get('HOST') + ':' + config.get('PORT'))
            config.update({'HOST_URL': http_tunnel.public_url})
            app.logger.debug(http_tunnel)
