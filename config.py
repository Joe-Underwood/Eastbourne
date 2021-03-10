import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SERVER_NAME = os.getenv('SERVER_NAME')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
