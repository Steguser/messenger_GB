from socket import *
import funcs
import select


# сформировать response сообщение
def response_msg(presence):
    if presence['action'] == 'presence':
        return {'response': '200'}
    elif presence['action'] == 'text':
        return {'response': presence['text_msg']}
    else:
        return {'response': '400'}


def mainloop():

    server = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    server.bind(('', 9999))  # Присваивает порт 8888
    # переходит в режим ожидания запросов (одновременно не более 100)
    server.listen(100)
    # ставим таймаут для переключения с accept
    server.settimeout(0.2)  # Таймаут для операций с сокетом

    # у нас будет много клиентов
    # создаем список клиентов
    clients = []

    while True:
        try:
            client, addr = server.accept()      # Принимает запрос на соединение
        except OSError as e:
            pass                                # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(client)  # Сохраняем клиента в список
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 0
            # who_writes = []
            # who_reads = []
            try:
                # начинаем мониторить что нужно сделать
                # кто нам пишет и кто читает
                who_writes, who_reads, e = select.select(clients, clients, clients, wait)

                for who_write in who_writes:                # кто нам написал
                    # print(who_write)                        # что нам написали
                    presence = funcs.get_message(who_write)    # Принимает сообщение
                    response = response_msg(presence)       # Формирует ответ
                for who_read in who_reads:                  # кто читает
                    # print(who_read)                         # что нам написали
                    if who_writes != []:
                        funcs.send_message(who_read, response)    # Отправляет ответ
                    else:
                        pass
            except:
                pass  # Ничего не делать, если какой-то клиент отключился


print('Эхо-сервер запущен!')
mainloop()
