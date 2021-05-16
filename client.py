from socket import *
import pickle

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
print(f"Сообщение от сервера: {msg_server}")
s.close()