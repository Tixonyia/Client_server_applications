from socket import *
import pickle

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(5)


while True:
    client, addr = s.accept()
    data = client.recv(1024)
    response = {
        'response': 200,
        'alert': 'Не очень нужное сообщение'
    }
    client.send(pickle.dumps(response))
    client.close()
    with open('data.txt', 'w') as dat:
        dat.write(str(s) + '\n')
        dat.write(str(pickle.loads(data)) + '\n')
        dat.write(str(response) + '\n')

