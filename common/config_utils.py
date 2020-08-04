import os
import configparser

conf_file = os.path.join(os.path.dirname(__file__),'..\conf\config.ini')

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(conf_file)

    @property
    def excel_path(self):
        excel_path = self.config.get('path', 'excel_path')
        return excel_path

config = Config()

if __name__ == '__main__':
    print(config.excel_path)


