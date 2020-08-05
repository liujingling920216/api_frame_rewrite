import logging

class Log:
    def __init__(self):
        self.logger = logging.getLogger('test.logs')
        self.logger.setLevel(level=10)
        self.format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    def streamlog(self):
        self.stream_log = logging.StreamHandler()
        self.stream_log.setFormatter(self.format)
        self.logger.addHandler(self.stream_log)
        return self.logger

    def filelog(self):
        self.file_log = logging.FileHandler('file.logs')
        self.file_log.setFormatter(self.format)
        self.logger.addHandler(self.file_log)
        return self.logger

log = Log().filelog()

if __name__ == "__main__":
    # logs.info('ceshi ')
    log.info('ceshi ')


