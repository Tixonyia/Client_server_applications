import pytest
import re


with open('data.txt') as file:
    s, msg, response = file.read().splitlines()
    family = re.search(r'family=\w*\S\w*', s).group(0)
    type_s = re.search(r'type=\w*\S\w*', s).group(0)


def test_socket_family():
    assert family == 'family=AddressFamily.AF_INET'


def test_socket_type():
    assert type_s == 'type=SocketKind.SOCK_STREAM'


def test_data():
    assert msg == "{'action': 'authenticate', 'time': '<unix timestamp>', 'user': {'account_name': 'WildCate', 'password': 'Think'}}"


def test_response():
    assert response == "{'response': 200, 'alert': 'Не очень нужное сообщение'}"
