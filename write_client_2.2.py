from socket import *
import time
import funcs


# создать presence сообщение
def create_presence():
    msg = {
        'action': 'presence',
        'time': time.time()
    }
    return msg


def create_text_msg():
    msg = {
        'action': 'text',
        'text_msg': input('Введите сообщение: ')
    }
    return msg


client = socket(AF_INET, SOCK_STREAM)       # Создать сокет TCP
client.connect(('localhost', 9999))         # Соединиться с сервером

presence_msg = create_presence()            # Создать presence сообщение
funcs.send_message(client, presence_msg)    # Отправить presence сообщение

response = funcs.get_message(client)        # Принять не более 1024 байтов данных
print(response)

while True:
    msg = create_text_msg()
    funcs.send_message(client, msg)
