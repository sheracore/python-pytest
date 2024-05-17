import configparser
from pathlib import Path


class ConfigFileParser:
    cfgFile = 'qa.ini'  # default config file
    cfgFileDirectory = 'config'  # default directory
    config = configparser.ConfigParser()

    def __init__(self, cfg=cfgFile):
        self.cfgFile = cfg
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfgFileDirectory).joinpath(self.cfgFile)
        self.config.read(self.CONFIG_FILE)

    def get_email_url(self):
        return self.config['gmail']['url']

    def get_email_user(self):
        return self.config['gmail']['user']

    def get_email_pass(self):
        return self.config['gmail']['pass']


if __name__ == '__main__':
    config = ConfigFileParser('qa.ini')
    print(config.get_email_pass())
    print(config.get_email_user())
