from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///messenger.db', echo=True, pool_recycle=7200)
Model = declarative_base(metadata=MetaData(bind=engine))
Session = sessionmaker(bind=engine)
