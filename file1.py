import logging

class Login:

    def __init__(self):
        self.logger = logging.getLogger('simple_example')
        logging.basicConfig(
            format='%(levelname)s:%(asctime)s :%(message)s', 
            datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
            
    def debug(self):
        logging.debug('This is a debug message')
        
    def info(self):
        logging.basicConfig(format='%(levelname)s:%(asctime)s:%(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
            
    def warning(self):
        logging.basicConfig(format='%(levelname)s:%(asctime)s:%(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.warning)
            
    def error(self):    
        logging.error('This is an error message')
        
    def critical(self):
        logging.critical('This is a critical message')