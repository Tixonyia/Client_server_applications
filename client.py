from socket import *
import pickle
import logging
import log.client_log_config

logger = logging.getLogger('client')

logger.debug('Start client successfully')
try:

    logger.debug('Start client successfully')

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 7777))
    msg = {
        "action": "authenticate",
        "time": "<unix timestamp>",
        "user": {
            "account_name": "WildCate",
            "password": "Think"
        }
    }
    s.send(pickle.dumps(msg))
    data = s.recv(1024)
    msg_server = pickle.loads(data)
    logger.debug("Message from server received")
    s.close()
    logger.debug('App client ending')
except:
    logger.critical('Boss, ull disappeared!!!')