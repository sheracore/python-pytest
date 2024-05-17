import configparser
from pathlib import Path

cfgFile = 'qa.ini'
cfgFileDirectory = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(cfgFile)

config.read(CONFIG_FILE)


def get_email_url():
    return config['gmail']['url']


def get_email_user():
    return config['gmail']['user']


def get_email_pass():
    return config['gmail']['pass']
