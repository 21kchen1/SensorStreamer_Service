import logging

class Log:

    @staticmethod
    def D(msg: str):
        logging.basicConfig(format= '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level= logging.DEBUG)
        logging.debug(msg)

    @staticmethod
    def I(msg: str):
        logging.basicConfig(format= '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level= logging.INFO)
        logging.info(msg)

    @staticmethod
    def W(msg: str):
        logging.basicConfig(format= '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level= logging.WARNING)
        logging.warning(msg)

    @staticmethod
    def E(msg: str):
        logging.basicConfig(format= '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level= logging.ERROR)
        logging.error(msg)

    @staticmethod
    def C(msg: str):
        logging.basicConfig(format= '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level= logging.CRITICAL)
        logging.critical(msg)