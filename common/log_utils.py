import os
import time
import logging
from common.config_utils import config

log_output_path = os.path.join(os.path.dirname(__file__),config.logs_path)

class Log:
    def __init__(self):
        self.log_name = os.path.join(log_output_path,'api_test_%s.logs'%(time.strftime('%Y_%m_%d')))
        self.logger = logging.getLogger('test.logs')
        self.logger.setLevel(config.logs_lever)
        self.format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


    def streamlog(self):
        stream_log = logging.StreamHandler()
        stream_log.setFormatter(self.format)
        self.logger.addHandler(stream_log)
        stream_log.close()
        return self.logger


    def filelog(self):
        file_log = logging.FileHandler(self.log_name,'a',encoding='utf-8')
        file_log.setFormatter(self.format)
        self.logger.addHandler(file_log)
        file_log.close()
        return self.logger

log = Log().filelog()

if __name__ == "__main__":
    # logs.info('ceshi ')
    log.info('ceshi ')