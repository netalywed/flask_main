import atexit
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, DateTime, Integer, String, create_engine, func
# from config import PG_DSN

engine = create_engine('postgresql://app:1234@127.0.0.1:5431/app') # engine = create_engine(PG_DSN)

Base = declarative_base(bind=engine)


class UserModel(Base):

    __tablename__ = "app_articles"

    art_id = Column(Integer, primary_key=True, autoincrement=True)
    headline = Column(String, unique=True, nullable=False, index=True)
    description = Column(String)
    creation_date = Column(DateTime, server_default=func.now())
    owner = Column(String, nullable=False)


Base.metadata.create_all()

Session = sessionmaker(bind=engine)


atexit.register(lambda: engine.dispose()) #закрывает БД после завершения работы приложения



# import uuid
# from typing import Type
#
# import config
# from cachetools import cached
# from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, create_engine, func
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy_utils import EmailType, UUIDType
#
# Base = declarative_base()
#
#
# class User(Base):
#
#     __tablename__ = "ads_users"
#
#     id = Column(Integer, primary_key=True)
#     email = Column(EmailType, unique=True, index=True)
#     password = Column(String(60), nullable=False)
#     registration_time = Column(DateTime, server_default=func.now())
#
#
# class Token(Base):
#
#     __tablename__ = "tokens"
#
#     id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
#     creation_time = Column(DateTime, server_default=func.now())
#     user_id = Column(Integer, ForeignKey("ads_users.id", ondelete="CASCADE"))
#     user = relationship("User", lazy="joined")
#
#
# @cached({})
# def get_engine():
#     return create_engine(config.PG_DSN)
#
#
# @cached({})
# def get_session_maker():
#     return sessionmaker(bind=get_engine())
#
#
# def init_db():
#     Base.metadata.create_all(bind=get_engine())
#
#
# def close_db():
#     get_engine().dispose()
#
#
# ORM_MODEL_CLS = Type[User] | Type[Token]
# ORM_MODEL = User | Token
