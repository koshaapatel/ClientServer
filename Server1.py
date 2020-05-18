import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 9999

    # create an INET, STREAMing socket
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    ServerSocket.bind((host, port))
    # become a server socket
    ServerSocket.listen(5)

    conn, address = ServerSocket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        received = conn.recv(1024)
        received = received.decode("utf-8")
        #data = conn.recv(1024).decode()
        if not received:
            # if data is not received break
            break
        #print("from connected user: " + str(data))
        print ("Received: {}".format(received))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()