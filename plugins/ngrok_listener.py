import atexit
from pyngrok import ngrok


class NgrokListener(object):

    def __init__(self, app=None):

        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if app is not None:
            self.app = app

        if self.app.config.get('ENVIRONMENT') == 'DEVELOPMENT':
            self.app.logger.debug(f'connecting to ngrok')
            # ngrok.kill()
            http_tunnel = ngrok.connect(bind_tls=True, addr=self.app.config.get('HOST') + ':' + self.app.config.get('PORT'))
            self.app.config.update({'HOST_URL': http_tunnel.public_url})
            self.app.logger.debug(http_tunnel)
        elif self.app.config.get('ENVIRONMENT') == 'PRODUCTION':
            self.app.logger.debug(f'setting up HOST_URL to heroku')
            heroku_app_name = self.app.config.get('HEROKU_APP_NAME')
            app.config.update({'HOST_URL': f'https://{heroku_app_name}.herokuapp.com'})

    #     self.app.teardown_appcontext(self.teardown)
            atexit.register(self.teardown)

    def teardown(self):
        if self.app.config.get('ENVIRONMENT') == 'DEVELOPMENT':
            tunnels = ngrok.get_tunnels()
            for tunnel in tunnels:
                ngrok.disconnect(tunnel.public_url)
            ngrok.kill()
