import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/note_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
