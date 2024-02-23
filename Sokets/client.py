import socket

def receive_file(socket, filename):
    with open(filename, 'wb') as f:
        while True:
            chunk = socket.recv(4096)
            if not chunk:
                break
            f.write(chunk)

def main():
    host = '127.0.0.1'
    port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    filename = input("Введите название файла: ")
    client_socket.send(filename.encode())

    receive_file(client_socket, filename)

    client_socket.close()