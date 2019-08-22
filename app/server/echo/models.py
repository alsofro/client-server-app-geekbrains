from sqlalchemy import Table, Column, Integer, DateTime, String
from sqlalchemy.orm import mapper

from db import database_metadata

message_table = Table(
    'messages', database_metadata,
    Column('id', Integer, primary_key=True),
    Column('content', String),
    Column('user', String),
    Column('created', DateTime)
)


class Message:
    def __init__(self, content, user, date):
        self.date = date
        self.user = user
        self.content = content


mapper(Message, message_table)
