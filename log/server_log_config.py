import logging
import os.path
from logging import handlers

logger = logging.getLogger('server')
formatter = logging.Formatter("%(created)f - %(filename)s - %(levelname)-12s - %(module)-12s - %(message)s ")

storage = 'logs'
if not os.path.exists(storage):
    os.mkdir(storage)
filename = os.path.join(storage, 'server.log')

fh = logging.handlers.TimedRotatingFileHandler(filename, encoding='utf-8', when='D', interval=1, backupCount=7)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования')