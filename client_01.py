# отправка presence сообщения

from socket import *
import time
import json

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect(('localhost', 8888))    # Соединиться с сервером

presence_message = {
    'action': 'presence',
    'time': time.time()
}

presence_message_json = json.dumps(presence_message)
presence_message_b = presence_message_json.encode('utf-8')
s.send(presence_message_b)


ans = json.loads(s.recv(1024).decode("utf-8"))['responce']        # Принять не более 1024 байтов данных
print(ans)
s.close()
