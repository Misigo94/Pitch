import os

class Config:
    DEBUG=True
    SECRET_KEY="Password"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
   


 # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class DevConfig(Config):
     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://user1:Password@localhost:5432/user1db'
    
    
        
class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


configurations = {"production":ProdConfig, "development":DevConfig}