from socket import *
import pickle
import logging
import log.client_log_config

logger = logging.getLogger('client')


def client():
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
        logger.debug(f"Message from server received: {msg_server}")
        s.close()
        logger.debug('App client ending')
    except:
        logger.critical('Boss, ull disappeared!!!')


if __name__ == '__main__':
    client()