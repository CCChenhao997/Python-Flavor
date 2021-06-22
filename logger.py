'''
Description: 
version: 
Author: chenhao
Date: 2021-06-22 16:18:08
'''
import logging
import coloredlogs


FIELD_STYLES = dict(
    asctime=dict(color='green'),
    hostname=dict(color='magenta'),
    levelname=dict(color='green'),
    filename=dict(color='magenta'),
    name=dict(color='blue'),
    threadName=dict(color='green')
)

LEVEL_STYLES = dict(
    debug=dict(color='green'),
    info=dict(color='cyan'),
    warning=dict(color='yellow'),
    error=dict(color='red'),
    critical=dict(color='red')
)

logger = logging.getLogger('tos')
coloredlogs.install(
    level="DEBUG",
    fmt="[%(asctime)s]:%(message)s",
    datefmt='%H:%M:%S',
    level_styles=LEVEL_STYLES,
    field_styles=FIELD_STYLES)


if __name__ == '__main__':
    # Use FileHandler to output the log to a file (test.log).
    fh = logging.FileHandler('test.log')
    fh.setLevel(logging.DEBUG)
    formatter_file = logging.Formatter(
        '%(asctime)s %(filename)s:%(lineno)d [%(levelname)s]: %(message)s',
        datefmt='%H:%M:%S')
    fh.setFormatter(formatter_file)
    logger.addHandler(fh)

    logger.debug('This is Debug mode')
    logger.info('This is info mode')
    logger.warning('This is warn mode')
    logger.error('This is error mode')
    logger.critical('This is critical mode')