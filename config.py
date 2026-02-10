import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DB_USER=os.getenv("DB_USER")
    DB_PASSWORD=quote_plus(os.getenv("DB_PASSWORD"))
    DB_HOST=os.getenv("DB_HOST")
    DB_NAME=os.getenv("DB_NAME")
    DB_PORT=os.getenv("DB_PORT")
    SQLALCHEMY_DATABASE_URI = (f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
