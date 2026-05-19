import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "clave-secreta-clinica"
    SQLALCHEMY_DATABASE_URI = "sqlite:///clinica.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True