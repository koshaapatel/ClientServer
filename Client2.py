import socket
import sys

if __name__ == '__main__':
    HOST, PORT = "localhost", 9999

    def printmenu():
        print(
            "Python DB Menu\n1. Find customer\n2. Add customer\n3. Delete customer\n4. Update customer age\n5. Update customer address\n6. Update customer phone\n7. Print report\n8. Exit")

    def performaction():
        printmenu()
        choice=int(input("Choice -> "))
        while choice != 8:
            if(choice>0 and choice<8):
                if(choice==1):
                    name = input("Enter name you want to search -> ")
                    list=["1"," ".join(name.lower().split())]
                    record=list[0]+" "+list[1]
                    clientsocket.sendall(bytes(record + "\n", "utf-8"))
                    print("Sent:     {}".format(record))
                    # Receive data from the server and shut down
                    received = str(clientsocket.recv(1024), "utf-8")
                    print("Received: {}".format(received))
                    printmenu()
                    choice = int(input("Choice -> "))
                if (choice == 2):
                    message = input(" -> ")
                    clientsocket.sendall(bytes(message + "\n", "utf-8"))
                    print("Sent:     {}".format(message))
                    # Receive data from the server and shut down
                    received = str(clientsocket.recv(1024), "utf-8")
                    print("Received: {}".format(received))
                    printmenu()
                    choice = int(input("Choice -> "))
                if (choice == 3):
                    printmenu()
                    choice = int(input("Choice -> "))
                if (choice == 4):
                    printmenu()
                    choice = int(input("Choice -> "))
                if (choice == 5):
                    printmenu()
                    choice = int(input("Choice -> "))
                if (choice == 6):
                    printmenu()
                    choice = int(input("Choice -> "))
                if (choice == 7):
                    printmenu()
                    choice = int(input("Choice -> "))
            elif(choice>=9 or choice<=0):
                break
            else:
                break

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
        # Connect to server and send data
        clientsocket.connect((HOST, PORT))

        performaction()

        clientsocket.close()