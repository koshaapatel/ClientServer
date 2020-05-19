import socket
import json
import sys

if __name__ == '__main__':
    HOST, PORT = "localhost", 9999

    def printmenu():
        print(
            "Python DB Menu\n1. Find customer\n2. Add customer\n3. Delete customer\n4. Update customer age\n5. Update customer address\n6. Update customer phone\n7. Print report\n8. Exit")


    #def printcustomerdata(printdata):


    def performaction():
        printmenu()
        choice=int(input("Choice -> "))
        printdata = {}
        while choice != 8:
            if(choice>0 and choice<8):
                if(choice==1):
                    name = input("Enter name you want to search -> ")
                    jsondata={"1":" ".join(name.lower().split())}
                    record = json.dumps(jsondata)
                    #clientsocket.sendall(bytes(jsondata, "utf-8"))
                    clientsocket.sendall(bytes(record, "utf-8")) #print("Sent:     {}".format(record))
                    # Receive data from the server and shut down
                    received = str(clientsocket.recv(1024), "utf-8")
                    dispatchreceived=received.split("\n")

                    if(dispatchreceived[0]=="1"):
                        loaded_json = json.loads(dispatchreceived[1])
                        print("Name        Age      Address               Telephone Number")
                        print("----        ----     -------               ----------------")
                        for x in loaded_json:
                            list=loaded_json[x]
                            print("%s" %(x),"       %s" %(list[0]),"       %s" %(list[1]),"        %s" %(list[2]))
                        #print("Received: {}".format(dispatchreceived[1]))
                    elif(dispatchreceived[0]=="0"):
                        print("Customer not found")

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
                    m = {"id": "2", "name": ""}  # a real dict.
                    data = json.dumps(m)
                    clientsocket.sendall(bytes(data,"utf-8"))
                    print("Sent:     {}".format(data))
                    # Receive data from the server and shut down
                    received = str(clientsocket.recv(1024), "utf-8")
                    print("Received: {}".format(received))
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
                print("You entered invalid value. Please enter valid option.")
                printmenu()
                choice = int(input("Choice -> "))
            else:
                print("You entered invalid value. Please enter valid option.")
                printmenu()
                choice = int(input("Choice -> "))

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
        # Connect to server and send data
        clientsocket.connect((HOST, PORT))

        performaction()

        clientsocket.close()