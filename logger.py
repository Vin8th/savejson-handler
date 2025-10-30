import logging

class Logger:
    """Custom logger class"""
    def __init__(self, filename='applicationlog.log'):
        # Creating an object
        self.logger = logging.getLogger(__name__)
        # Setting the threshold of logger to DEBUG
        self.logger.setLevel(logging.DEBUG)

        # Check if handlers already exist to avoid duplicate logs
        if not self.logger.handlers:
            # StreamHandler for terminal output
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.DEBUG)
            stream_formatter = logging.Formatter('%(message)s')
            stream_handler.setFormatter(stream_formatter)

            # FileHandler for logging to a file
            file_handler = logging.FileHandler(filename)
            file_handler.setLevel(logging.DEBUG)
            file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)

            # Adding handlers to the Logger
            self.logger.addHandler(stream_handler)
            self.logger.addHandler(file_handler)
    
    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
    
    def debug(self, message):
        self.logger.debug(message)

    def critical(self, message):
        self.logger.critical(message)