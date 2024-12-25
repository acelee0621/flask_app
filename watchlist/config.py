import os

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg://postgres:postgres@localhost:5432/flask'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv('SECRET_KEY', 'dev')