import logging


class LogGen:
    @staticmethod
    def loggen():
        #basic config to contain the file name and its format
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
        handler =  logging.FileHandler(filename = ".\\Logs\\automation.log")
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        # this will provide any infor warning
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger