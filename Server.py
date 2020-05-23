import socketserver
import re
import json

class MyTCPHandler(socketserver.BaseRequestHandler):
    def senddata(self):
        flag = 0
        for key in database.customer:
            if (key != ''):
                flag = 1
                forwarddata = database.customer
                forwarddata = json.dumps(forwarddata, sort_keys=True)
                self.request.sendall(
                    bytes("1\nPrint Report:\n" + forwarddata, "utf-8"))
                break
        if (flag == 0):
            forwarddata = database.customer
            forwarddata = json.dumps(forwarddata, sort_keys=True)
            self.request.sendall(
                bytes("0\nNo records to display" + forwarddata, "utf-8"))

    # The request handler class for our server. It is instantiated once per connection to the server, and must override the handle() method to implement communication to the client.
    def handle(self):  # print(database.customer.keys()) print(database.customer.values())
        while True:
            self.data = self.request.recv(1024)
            if not self.data:
                print("Client is disconnected")
                break

            # print(self.data) #data in bytes
            loaded_json = json.loads(self.data)
            forwarddata = {}
            for x in loaded_json:  # print("choice:%s" % (x))
                received = str(self.data, "utf-8")
                if (x == "1"):
                    lookupname = loaded_json[x]
                    flag = 0  # not found
                    for custdata in database.customer:
                        if (custdata == lookupname):
                            forwarddata[custdata] = database.customer[custdata]
                            forwarddata = json.dumps(forwarddata)
                            self.request.sendall(
                                bytes("1\nFollowing is the customer record found:\n" + forwarddata,
                                      "utf-8"))
                            flag = 1
                            break
                    if (flag == 0):
                        self.request.sendall(bytes("0\nCustomer not found", "utf-8"))

                elif (x == "2"):
                    flag = 1  # we added customer
                    loaded = loaded_json[x]  # json key
                    for key in loaded:
                        for custdata in database.customer:
                            if (key == custdata):
                                flag = 0
                                break
                        if (flag == 0):
                            self.request.sendall(bytes("0\nCustomer already exists", "utf-8"))
                        else:
                            values = loaded[key]
                            if not values[0]:
                                values[0] = None
                            if not values[1]:
                                values[1] = None
                            if not values[2]:
                                values[2] = None
                            database.customer[key] = values
                            forwarddata[key] = database.customer[key]
                            forwarddata = json.dumps(forwarddata)
                            self.request.sendall(
                                bytes("1\nCustomer is added as below\n" + forwarddata,
                                      "utf-8"))

                elif (x == "3"):
                    lookupname = loaded_json[x]
                    flag = 0  # not found
                    for custdata in database.customer:
                        if (custdata == lookupname):
                            del database.customer[custdata]
                            forwarddata = database.customer
                            forwarddata = json.dumps(forwarddata, sort_keys=True)
                            self.request.sendall(bytes("1\nCustomer is deleted\n" + forwarddata, "utf-8"))
                            flag = 1
                            break
                    if (flag == 0):
                        self.request.sendall(
                            bytes("0\nCustomer doesn't exist therefore, we can't delete customer", "utf-8"))

                elif (x == "4"):
                    lookupnameage = loaded_json[x]
                    flag = 0  # not found
                    for custdata in database.customer:
                        if (custdata == lookupnameage[0]):
                            # for keys in database.customer:
                            values = database.customer[custdata]
                            if lookupnameage[1] == "":
                                values[0] = None
                                database.customer[custdata] = values
                                flag = 1
                                break
                            else:
                                values[0] = lookupnameage[1]
                                database.customer[custdata] = values
                                flag = 1
                                break
                    if (flag == 1):
                        forwarddata = database.customer
                        forwarddata = json.dumps(forwarddata, sort_keys=True)
                        self.request.sendall(
                            bytes("1\nCustomer's age is updated\n" + forwarddata,
                                  "utf-8"))
                    elif (flag == 0):
                        self.request.sendall(
                            bytes("0\nCustomer doesn't exist therefore, we can't update customer's age", "utf-8"))

                elif (x == "5"):
                    lookupnameaddress = loaded_json[x]
                    flag = 0  # not found
                    for custdata in database.customer:
                        if (custdata == lookupnameaddress[0]):
                            # for keys in database.customer:
                            values = database.customer[custdata]
                            if lookupnameaddress[1] == "":
                                values[1] = None
                                database.customer[custdata] = values
                                flag = 1
                                break
                            else:
                                values[1] = lookupnameaddress[1]
                                database.customer[custdata] = values
                                flag = 1
                                break
                    if (flag == 1):
                        forwarddata = database.customer
                        forwarddata = json.dumps(forwarddata, sort_keys=True)
                        self.request.sendall(
                            bytes("1\nCustomer's address is updated\n" + forwarddata,
                                  "utf-8"))
                    elif (flag == 0):
                        self.request.sendall(
                            bytes("0\nCustomer doesn't exist therefore, we can't update customer's address", "utf-8"))

                elif (x == "6"):
                    lookupnametelephone = loaded_json[x]
                    flag = 0  # not found
                    for custdata in database.customer:
                        if (custdata == lookupnametelephone[0]):
                            # for keys in database.customer:
                            values = database.customer[custdata]
                            if lookupnametelephone[1] == "":
                                values[2] = None
                                database.customer[custdata] = values
                                flag = 1
                                break
                            else:
                                values[2] = lookupnametelephone[1]
                                database.customer[custdata] = values
                                flag = 1
                                break
                    if(flag==1):
                        forwarddata = database.customer
                        forwarddata = json.dumps(forwarddata, sort_keys=True)
                        self.request.sendall(
                                bytes("1\nCustomer's telephone number is updated\n" + forwarddata,
                                      "utf-8"))
                    elif (flag == 0):
                        self.request.sendall(
                            bytes("0\nCustomer doesn't exist therefore, we can't update customer's telephone number",
                                  "utf-8"))

                elif (x == "7"):
                    self.senddata()

class SingletonDatabase(object):
    _instance = None
    customer = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonDatabase, cls).__new__(cls)
        return cls._instance

    def loaddatabase(self):
        file1 = open('data.txt', 'r')
        count = 0

        while True:
            count += 1
            line = file1.readline()

            if not line:
                break
            tempdata = line.split("|")
            customerdata = []
            if (re.findall("[a-z]", " ".join(tempdata[0].lower().split())) and tempdata[
                0] != ''):
                if not tempdata[1]:
                    customerdata.append(None)
                else:
                    customerdata.append(" ".join(tempdata[1].lower().split()))

                if not tempdata[2]:
                    customerdata.append(None)
                else:
                    customerdata.append(" ".join(tempdata[2].lower().split()))

                if not tempdata[3] or tempdata[3] == '\n':
                    customerdata.append(None)
                else:
                    customerdata.append(" ".join(tempdata[3].lower().split()))

                # customerdata = [" ".join(tempdata[1].lower().split()), " ".join(tempdata[2].lower().split()),
                #                 " ".join(tempdata[3].lower().split())]
                self.customer[" ".join(tempdata[0].lower().split())] = customerdata

            elif (tempdata[0] == ''):
                print("Database record is skipped")
        file1.close()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    database = SingletonDatabase()
    database.loaddatabase()

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as serversocket:
        # Activate the server; this will keep running until you # interrupt the program with Ctrl-C
        serversocket.serve_forever()

    def exit():
        serversocket.server_close()