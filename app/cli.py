import click
from app import db
from app.models import models_list
from flask.cli import with_appcontext


def register(app):

    @app.cli.group()
    def database():
        pass

    @database.command('init')
    @with_appcontext
    def init_db_command():
        # with db:
        db.create_tables(models_list)
        click.echo('Initialized the database.')

    @database.command('drop')
    @with_appcontext
    def drop_db_command():
        # with db:
        db.drop_tables(models_list)
        click.echo('Dropped the database.')
