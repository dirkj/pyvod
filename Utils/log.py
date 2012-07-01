import logging
import logging.config


def is_debug():
    log = get_logger()
    return log.level <= logging.DEBUG

def get_logger(name="pyvod"):
    logging.config.fileConfig('Resources/vodlog.conf')
    logger = logging.getLogger(name)
    return logger

