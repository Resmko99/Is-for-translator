import socket

def send_file(conn, filename):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            conn.sendall(chunk)

def main():
    host = '127.0.0.1'
    port = 9999 #Порт открыт только на моих устройствах.

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Сервер смотрит порт", port)

    conn, addr = server_socket.accept()
    print("Соединение:", addr)

    filename = input("Введите файл для отправки: ")
    send_file(conn, filename)

    conn.close()
    server_socket.close()