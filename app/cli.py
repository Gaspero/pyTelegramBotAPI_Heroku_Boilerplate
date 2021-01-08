import click
from flask.cli import with_appcontext


def register(app):

    @app.cli.group()
    def database():
        pass

    @database.command('init')
    @with_appcontext
    def init_db_command():
        # init db here
        click.echo('Initialized the database.')

    @database.command('drop')
    @with_appcontext
    def drop_db_command():
        # drop db here
        click.echo('Dropped the database.')
