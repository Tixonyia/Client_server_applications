from socket import socket, AF_INET, SOCK_STREAM
import pickle
import logging
import log.client_log_config
from decorators import log_dec


logger = logging.getLogger('client')
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

msg_server = None


@log_dec
def client():
    try:
        s.send(pickle.dumps(msg))
        data = s.recv(1024)
        msg_server = pickle.loads(data)
        logger.debug(f"Message from server received: {msg_server}")
        s.close()
        logger.debug('App client ending')
    except:
        logger.critical('Boss, ull disappeared!!!')


client()