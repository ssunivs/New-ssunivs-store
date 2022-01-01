import os

import dotenv

dotenv.load_dotenv(verbose=True)

APP_NAME = os.environ.get("APP_NAME", "SSUNIVS")

# Database
__DB_USER__ = os.environ.get("DB_USER")
__DB_PASSWORD__ = os.environ.get("DB_PASSWORD")
__DB_HOST__ = os.environ.get("DB_HOST")
__DB_PORT__ = os.environ.get("DB_PORT")
__DB_NAME__ = os.environ.get("DB_NAME")

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{__DB_USER__}:{__DB_PASSWORD__}@{__DB_HOST__}:{__DB_PORT__}/{__DB_NAME__}?charset=utf8"

# Auth
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
