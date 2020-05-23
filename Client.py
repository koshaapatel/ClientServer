import socket
import json
import re

if __name__ == '__main__':
    HOST, PORT = "localhost", 9999

    def printmenu():
        print(
            "\nPython DB Menu\n1. Find customer\n2. Add customer\n3. Delete customer\n4. Update customer age\n5. Update customer address\n6. Update customer phone\n7. Print report\n8. Exit")

    def printcustomerdata(printdata):
        loaded_json = json.loads(printdata)
        print("Name        Age      Address               Telephone Number")
        print("----        ----     -------               ----------------")
        for x in loaded_json:
            if (x != ''):
                list = loaded_json[x]
                print("%s" % (x), "       %s" % (list[0]), "       %s" % (list[1]), "        %s" % (list[2]))
            elif (x == ''):
                print("No record to display")

    def receivedata():
        received = str(clientsocket.recv(1024), "utf-8")
        dispatchreceived = received.split("\n")
        if (dispatchreceived[0] == "1"):
            print(dispatchreceived[1])
            printcustomerdata(dispatchreceived[2])
        elif (dispatchreceived[0] == "0"):
            print(dispatchreceived[1])

    def printmessage():
        received = str(clientsocket.recv(1024), "utf-8")
        dispatchreceived = received.split("\n")
        if (dispatchreceived[0] == "1"):
            print(dispatchreceived[1])
        elif (dispatchreceived[0] == "0"):
            print(dispatchreceived[1])

    def performaction():
        printmenu()
        select = input("Select -> ")
        select = " ".join(select.lower().split())
        while select != "8":
            select = " ".join(select.lower().split())
            dispatchreceived = []
            if (select == "1"):
                while True:
                    name = input("Enter name you want to search -> ")
                    if (re.findall("[a-z]", " ".join(name.lower().split())) and name != ''):
                        jsondata = {"1": " ".join(name.lower().split())}
                        record = json.dumps(jsondata)
                        # clientsocket.sendall(bytes(jsondata, "utf-8"))
                        clientsocket.sendall(bytes(record, "utf-8"))
                        # Receive data from the server and shut down
                        received = str(clientsocket.recv(1024), "utf-8")
                        dispatchreceived = received.split("\n")

                        if (dispatchreceived[0] == "1"):
                            print(dispatchreceived[1])
                            printcustomerdata(dispatchreceived[2])
                            break
                        elif (dispatchreceived[0] == "0"):
                            print(dispatchreceived[1])
                            break
                    else:
                        print("Invalid name")

                printmenu()
                select = input("Select -> ")

            elif (select == "2"):
                tempdata = []
                while True:
                    name = input("Enter name -> ")
                    if (re.findall("[a-z]", " ".join(name.lower().split())) and name != ''):
                        break
                    else:
                        print("Invalid name")
                while True:
                    age = input("Enter age -> ")
                    if (re.findall("[0-9]",
                                   " ".join(age.lower().split())) or age == ''):  # if(age.isdigit() or age==''):
                        age=re.sub("\D", "", " ".join(age.lower().split()))
                        break
                    else:
                        print("Invalid age")
                address = input("Enter address -> ")
                telephone = input("Enter telephone number -> ")
                tempdata = [" ".join(age.lower().split()), " ".join(address.lower().split()),
                            " ".join(telephone.lower().split())]

                jsondata = {"2": {" ".join(name.lower().split()): tempdata}}
                record = json.dumps(jsondata)
                clientsocket.sendall(bytes(record, "utf-8"))

                receivedata()

                printmenu()
                select = input("Select -> ")

            elif (select == "3"):
                while True:
                    name = input("Enter name you want to delete -> ")
                    if (re.findall("[a-z]", " ".join(name.lower().split())) and name != ''):
                        jsondata = {"3": " ".join(name.lower().split())}
                        record = json.dumps(jsondata)
                        clientsocket.sendall(bytes(record, "utf-8"))

                        printmessage()
                        break
                    else:
                        print("Invalid name")
                        break

                printmenu()
                select = input("Select -> ")
            elif (select == "4"):
                while True:
                    name = input("Enter name -> ")
                    if (re.findall("[a-z]", " ".join(name.lower().split())) and name != ''):
                        break
                    else:
                        print("Invalid name")
                while True:
                    age = input("Enter age -> ")
                    if (re.findall("[0-9]",
                                   " ".join(age.lower().split())) or age == ''):  # if (age.isdigit() or age == ''):
                        age = re.sub("\D", "", " ".join(age.lower().split()))
                        break
                    else:
                        print("Invalid age")
                nameage = [" ".join(name.lower().split()), " ".join(age.lower().split())]

                jsondata = {"4": nameage}
                record = json.dumps(jsondata)
                clientsocket.sendall(bytes(record, "utf-8"))

                printmessage()

                printmenu()
                select = input("Select -> ")
            elif (select == "5"):
                while True:
                    name = input("Enter name -> ")
                    if (re.findall("[a-z]", " ".join(name.lower().split())) and name != ''):
                        break
                    else:
                        print("Invalid name")

                address = input("Enter address -> ")
                nameaddress = [" ".join(name.lower().split()), " ".join(address.lower().split())]

                jsondata = {"5": nameaddress}
                record = json.dumps(jsondata)
                clientsocket.sendall(bytes(record, "utf-8"))

                printmessage()

                printmenu()
                select = input("Select -> ")
            elif (select == "6"):
                while True:
                    name = input("Enter name -> ")
                    if (re.findall("[a-z]", " ".join(name.lower().split())) and name != ''):
                        break
                    else:
                        print("Invalid name")

                telephone = input("Enter telephone number -> ")
                nametelephone = [" ".join(name.lower().split()), " ".join(telephone.lower().split())]

                jsondata = {"6": nametelephone}
                record = json.dumps(jsondata)
                clientsocket.sendall(bytes(record, "utf-8"))

                printmessage()

                printmenu()
                select = input("Select -> ")
            elif (select == "7"):
                jsondata = {"7": "print report"}
                record = json.dumps(jsondata)
                clientsocket.sendall(bytes(record, "utf-8"))

                receivedata()

                printmenu()
                select = input("Select -> ")
            else:
                print("You entered invalid value. Please enter valid option.")
                printmenu()
                select = input("Select -> ")
        if (select == "8"):
            print("Good bye")

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
    # Connect to server and send data
    clientsocket.connect((HOST, PORT))

    performaction()

    clientsocket.close()