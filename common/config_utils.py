import os
import configparser

conf_file = os.path.join(os.path.dirname(__file__),'../conf/config.ini')

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(conf_file,encoding='utf-8')

    @property
    def excel_path(self):
        excel_path = self.config.get('PATH', 'excel_path')
        return excel_path

    @property
    def logs_path(self):
        log_path = self.config.get('PATH', 'log_path')
        return log_path

    @property
    def logs_lever(self):
        log_lever = int(self.config.get('LOG','log_lever'))
        return log_lever

    @property
    def hosts(self):
        host = self.config.get('DEFAULT','host')
        return host

config = Config()

if __name__ == '__main__':
    print(config.excel_path)
    print(config.logs_path)
    print(config.hosts)


