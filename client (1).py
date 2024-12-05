import socket

PORT = 5432
ADDRESS = '127.0.0.1'


if __name__ == '__main__':
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect((ADDRESS, PORT))

    print('Connected to server on address', ADDRESS)
    print('Hello')

    try:
        c_socket.sendall('Hello server'.encode('ascii'))
    except socket.error:
        pass
    else:
        response = c_socket.recv(1024)

        if response == b'':
            # Error
            pass
        else:
            print('Server sent:', response.decode('ascii'))
            c_socket.close()
