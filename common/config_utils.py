import os
import configparser

conf_file = os.path.join(os.path.dirname(__file__),'../conf/config.ini')

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(conf_file)

    @property
    def excel_path(self):
        excel_path = self.config.get('PATH', 'excel_path')
        return excel_path

    @property
    def logs_path(self):
        log_path = self.config.get('PATH', 'log_path')
        return log_path

    @property
    def log_lever(self):
        log_lever = int(self.config.get('LOG','log_lever'))
        return log_lever

config = Config()

if __name__ == '__main__':
    print(config.excel_path)
    print(config.logs_path)


