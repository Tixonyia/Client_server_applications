import pytest
import os

from client_file import s,  msg, msg_server


def test_socket_family():
    assert str(s.family) == 'AddressFamily.AF_INET'


def test_socket_type():
    assert str(s.type) == 'SocketKind.SOCK_STREAM'


def test_msg():
    assert msg == {
                    "action": "authenticate",
                    "time": "<unix timestamp>",
                    "user": {
                        "account_name": "WildCate",
                        "password": "Think"
                    }}


def test_msg_server():
    assert msg_server == {
                            "response": 200,
                            "alert": "Не очень нужное сообщение"
                        }



