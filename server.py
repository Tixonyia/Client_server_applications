import logging
from socket import *
import pickle
import log.server_log_config


logger = logging.getLogger('server')

try:
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 7777))
    s.listen(5)

    while True:
        logger.debug('Start server successfully')
        client, addr = s.accept()
        data = client.recv(1024)
        response = {
            'response': 200,
            'alert': 'Не очень нужное сообщение'
        }
        client.send(pickle.dumps(response))
        client.close()
        logger.debug('App server ending')
        logger.debug('Save in data start')
        with open('tests/data.txt', 'w') as dat:
            dat.write(str(s) + '\n')
            dat.write(str(pickle.loads(data)) + '\n')
            dat.write(str(response) + '\n')
        logger.debug('Save in data end')

except:
    logger.critical('Boss, ull disappeared!!!')
