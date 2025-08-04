#!/usr/bin/env python3
import logging
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._setup_logger()
        return cls._instance
    
    def _setup_logger(self):

        self.logger = logging.getLogger("AppLogger")
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.hasHandlers():
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)

            self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger
    

if __name__ == '__main__':
    logger = Logger().get_logger()
    logger.info("This is a info log")