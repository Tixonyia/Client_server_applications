import sys
import logging
import threading
import select
import chat.chat as chat
import chat.base as base
import log.client_log_config

logger = logging.getLogger('chat.client')


def msg_def():
    msg = input('Введите тип сообщения "П" - пользователю, "Г" - группе, "ВГ" - выбор группы: ')
    if msg == "ВГ":
        group = input("Введите номер группы, в которую вы хотите вступить или создать: ")
        if group not in base.GROUPS:
            base.GROUPS['name'] = group
        if group in base.GROUPS:
            base.GROUPS['members'].append(client_name)
        base.MESSAGE['to'] = base.GROUPS['members']
    elif msg == "П":
        person = input("Введите имя пользователя: ")
        base.GROUPS['members'] = [person]
        base.MESSAGE['to'] = base.GROUPS['members']
        base.GROUPS['message'] = msg
    elif msg == "Г":
        base.GROUPS['name'] = msg
        if client_name in base.GROUPS['members']:

            base.GROUPS['message'] = msg
        else:
            print('Вступите в группу')


def send(sock):
    msg_def()
    while True:
        msg = input('Введите сообщение ("exit" для выхода): ')
        if msg:
            print(msg)
            base.MESSAGE['message'] = msg

            try:
                chat.send_data(sock, base.MESSAGE)
            except ConnectionResetError as e:
                logger.error(e)
                break


def receive(sock):
    while True:
        try:
            data = chat.get_data(sock)
        except ConnectionResetError as e:
            logger.error(e)
            break

        if data['response'] != '200':
            logger.debug('App ending')
            break

        if 'messages' in data:
            for message in data['messages']:
                sys.stdout.write(f'{message["time"]} - {message["from"]}: {message["message"]}')


if __name__ == '__main__':
    logger.debug('App started')

    parser = chat.create_parser()
    namespace = parser.parse_args()

    client_name = input('Введите имя: ')

    sock = chat.get_client_socket(namespace.addr, namespace.port)
    serv_addr = sock.getpeername()
    start_info = f'Connected to server: {serv_addr[0]}:{serv_addr[1]}'
    print(start_info)
    logger.info(start_info)

    base.PRESENCE['user']['account_name'] = client_name
    try:
        chat.send_data(sock, base.PRESENCE)
    except ConnectionResetError as e:
        logger.error(e)
        sock.close()
        exit(1)

    p_send = threading.Thread(target=send, args=(sock,))
    p_receive = threading.Thread(target=receive, daemon=True, args=(sock,))

    p_send.start()
    p_receive.start()

    p_send.join()
    p_receive.join()
    sock.close()