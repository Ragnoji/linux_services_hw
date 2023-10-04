import socket
from datetime import datetime
from threading import Thread


def handle_connection(connection):
    try:
        connection.send(datetime.now().strftime("%d.%m.%Y %H:%M").encode('utf-8'))
        connection.close()
    except Exception:
        return


if __name__ == '__main__':
    addr = ("", 1303)
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    sock.bind(addr)
    sock.listen(8)

    while True:
        conn_pair = sock.accept()
        Thread(target=handle_connection, args=(conn_pair[0],)).start()
