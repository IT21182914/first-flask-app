import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://dilan:1234@localhost/note_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
