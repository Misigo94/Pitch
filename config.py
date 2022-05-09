from distutils.command.config import config
import os

class Config:
     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://martin:Misigouts94@localhost:5432/Pitch'
     DEBUG = True

class DevConfig(Config):
    pass

class ProdConfig(Config):
    pass



