import os
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    parentdir = os.path.dirname(basedir)
    
    # Use SQLite database for local development
    databaseuri = 'sqlite:///' + os.path.join(parentdir, 'school.db')
    print(f"Using database URI: {databaseuri}")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", databaseuri)
