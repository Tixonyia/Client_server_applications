from functools import wraps
from inspect import stack
import logging

logger_client = logging.getLogger('client')
logger_server = logging.getLogger('server')


def log_dec(func):
    logger_server.debug(f'Function "{func.__name__}" is called into "{stack()[1][1]}"')
    logger_client.debug(f'Function "{func.__name__}" is called into "{stack()[1][1]}"')
    @wraps(func)
    def call(*args, **kwargs):
        logger_server.debug(f'Function "{func.__name__}" is called into "{stack()[1][3]}"')
        logger_client.debug(f'Function "{func.__name__}" is called into "{stack()[1][3]}"')
        return func(*args, **kwargs)
    return call()

