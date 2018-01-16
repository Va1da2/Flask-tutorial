"Configuration file."
import os


class Config(object):
    "Class for general config"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"