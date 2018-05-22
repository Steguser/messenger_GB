# Программа сервера времени
from socket import *
import time
import json

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('', 8888))                # Присваивает порт 8888
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # одновременно обслуживает не более
                                  # 5 запросов.


def get_message(msg):
    bmessage = msg.recv(1024)
    result_json = bmessage.decode('utf-8')
    result = json.loads(result_json)
    return result

def send_message(client, responce):
    result_json = json.dumps(responce_message)
    result_b = result_json.encode('utf-8')
    client.send(result_b)

while True:
    client, addr = s.accept()     # Принять запрос на соединение
    print(client)
    print(addr)
    presence = get_message(client)
    print(presence)

    if presence['action'] == 'presence':
        responce_message = {
            'responce': '200'
        }
    else:
        responce_message = {
            'responce': '400'
        }

    #responce = presence_responce(presence)
    send_message(client, responce_message)

    
    # Дальнейшая работа ведётся с сокетом клиента

    client.close()

