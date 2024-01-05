import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://example:example@db/example'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
