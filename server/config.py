import os

class Config:
    # base directory of the application
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # sqlite database file path
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'instance', 'late_show.db')
    
    # disable sqlalchemy event system
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # secret key for session management
    SECRET_KEY = 'your_secret_key_here'
    