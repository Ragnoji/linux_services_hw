import socket

if __name__ == '__main__':
    address = input('Введите ipv4-адресс сервера\n')
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            conn.connect((address, 1303))
            break
        except OSError:
            address = input('Произошла ошибки при подключении, введите адрес заново\n')
            continue
    data = conn.recv(1024)
    print(data.decode('utf-8'))
    conn.close()
