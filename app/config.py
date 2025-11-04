import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'chave-padrao-insegura')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-chave-padrao')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    
    # SQLite (simples para começar)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///tarefas.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
