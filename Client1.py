import socket

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 9999  # socket server port number

    # create an INET, STREAMing socket
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    ClientSocket.connect((host, port))

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        ClientSocket.send(message.encode())  # send message
        data = ClientSocket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    ClientSocket.close()  # close the connection


if __name__ == '__main__':
    client_program()
