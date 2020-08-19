import logging

logging.basicConfig(level=logging.DEBUG)


def logentry(func):
    def wrapper():
        logging.info("Starting " + func.__name__)
        func()
        logging.info("Stopping " + func.__name__)
    return wrapper