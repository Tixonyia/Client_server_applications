from socket import *
import pickle

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(5)


while True:
    client, addr = s.accept()
    data = client.recv(1024)
    print(pickle.loads(data))
    response = {
        "response": 200,
        "alert": "Не очень нужное сообщение"
    }
    client.send(pickle.dumps(response))
    client.close()