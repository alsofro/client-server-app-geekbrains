from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///messenger.db', echo=True, pool_recycle=7200)
Model = declarative_base()


class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    info = Column(String)

    def __init__(self, login, info):
        self.login = login
        self.info = info


class ClientHistory(Model):
    __tablename__ = 'client_history'
    id = Column(Integer, primary_key=True)
    entry_time = Column(String)
    ip_addr = Column(String)

    def __init__(self, entry_time, ip_addr):
        self.entry_time = entry_time
        self.ip_addr = ip_addr


class ContactList(Model):
    __tablename__ = 'contact_list'
    id = Column(Integer, primary_key=True)
    owner_id = Column(String)
    client_id = Column(String)

    def __init__(self, owner_id, client_id):
        self.owner_id = owner_id
        self.client_id = client_id

database_metadata = MetaData()