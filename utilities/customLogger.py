import logging

class LogGen:
    @staticmethod
    def loggen():
        #logging.basicConfig(filename=".//Logs//automation.log", filemode='a', level="INFO",
        #                    format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #logger=logging.getLogger()
        #logger.setLevel(logging.INFO)
       # return logger
        # logger = logging.getLogger('demologger')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler(".//Logs//automation.log", mode='w')
        fileHandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger