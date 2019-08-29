from sqlalchemy import create_engine, Column, Integer, String, MetaData, DateTime

from db import Model

from datetime import datetime

class Message(Model):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    data = Column(String, nullable=True)
    created = Column(DateTime, default=datetime.now())