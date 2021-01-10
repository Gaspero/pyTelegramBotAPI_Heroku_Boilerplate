import datetime
from app import db


from peewee import *


class BaseModel(Model):
    class Meta:
        database = db

    created_date = DateTimeField(default=datetime.datetime.now)


class User(BaseModel):

    chat_id = TextField(primary_key=True)
    id = TextField()
    first_name = TextField()
    last_name = TextField()
    username = TextField()

    def __str__(self):
        return f'username: {self.username} id: {self.id}'


models_list = [User]
