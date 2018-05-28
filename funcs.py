import json


# функция перевода Dict -> Bytes
def dict_to_b(msg):
    msg_json = json.dumps(msg)
    msg_b = msg_json.encode('utf-8')
    return msg_b


# функция перевода Bytes -> Dict
def b_to_dict(msg_b):
    msg_json = msg_b.decode('utf-8')
    msg = json.loads(msg_json)
    return msg


# отправить сообщение
def send_message(sock, message):
    # Словарь переводим в байты
    presence_b = dict_to_b(message)
    # Отправляем
    sock.send(presence_b)


# принять сообщение
def get_message(sock):
    # Получаем байты
    response_b = sock.recv(1024)
    # переводим байты в словарь
    response = b_to_dict(response_b)
    # возвращаем словарь
    return response
