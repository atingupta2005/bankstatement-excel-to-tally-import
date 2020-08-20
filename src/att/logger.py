import logging
from functools import wraps

def create_logger(level=logging.INFO):
    # create a logger object
    logger = logging.getLogger('exc_logger')
    logger.setLevel(level)

    # create a file to store all the
    # logged exceptions
    logfile = logging.FileHandler('logs/exc_logger.log')

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)

    logfile.setFormatter(formatter)
    logger.addHandler(logfile)

    return logger

def exception(logger):
    # logger is the logging object
    # exception is the decorator objects
    # that logs every exception into log file
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            try:
                logger.info("Starting " + func.__name__)
                rt = func(*args, **kwargs)
                logger.info("Stopping " + func.__name__)
                return rt
            except:
                issue = "exception in " + func.__name__ + "\n"
                issue = issue + "-------------------------\
                ------------------------------------------------\n"
                logger.exception(issue)
            raise

        return wrapper

    return decorator