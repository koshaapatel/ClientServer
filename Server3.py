import socketserver
import re
import json

class MyTCPHandler(socketserver.BaseRequestHandler):
    # The request handler class for our server.It is instantiated once per connection to the server, and must override the handle() method to implement communication to the client.
    def handle(self):
        print(database.customer.keys())
        print(database.customer.values())
        while True:
            self.data = self.request.recv(1024)
            if not self.data:
                print("client is gone")
                break
            # print("{} wrote:".format(self.client_address[0])) # print("{} wrote:".format(self.client_address[1])) # received = self.data.decode("utf-8")
            print("while true")
            print(self.data) #data in byte
            loaded_json = json.loads(self.data)
            forwarddata = {}
            for x in loaded_json:
                print("choice:%s" % (x))
                received = str(self.data, "utf-8")  # received = received.decode("utf-8")
                # print("%s: %s" % (x, loaded_json[x]))
                if (x == "1"):
                    print("Received: {}".format(received))
                    lookupname = loaded_json[x]
                    flag=0 #not found
                    for custdata in database.customer:
                        if (custdata == lookupname):
                            # alldata=database.customer[custdata]
                            forwarddata[custdata] = database.customer[custdata]
                            forwarddata = json.dumps(forwarddata)
                            self.request.sendall(bytes("1\n" + forwarddata, "utf-8"))
                            print("Sent:     {}".format(forwarddata))
                            flag=1
                            break
                    if(flag==0):
                        self.request.sendall(bytes("0", "utf-8"))

                elif (x == "2"):
                    flag = 1#we added customer
                    #print("Received: {}".format(received))
                    loaded = loaded_json[x] #json
                    for key in loaded:
                        for custdata in database.customer:
                            if (key == custdata):
                                flag=0
                                break
                        if(flag==0):
                            self.request.sendall(bytes("0", "utf-8"))
                        else:
                            database.customer[key]=loaded[key]
                            forwarddata[key] = database.customer[key]
                            forwarddata = json.dumps(forwarddata)
                            self.request.sendall(bytes("1\n" + forwarddata, "utf-8"))
                            print(database.customer)
                            print("Sent:     {}".format(forwarddata))
                            print(database.customer.keys())
                            print(database.customer.values())

                elif (x == "3"):
                    print("3")
                elif (x == "4"):
                    print("4")
                elif (x == "5"):
                    print("5")
                elif (x == "6"):
                    print("6")
                elif (x == "7"):
                    print("7")


class SingletonDatabase(object):
    _instance = None
    customer = {}

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(SingletonDatabase, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

    def loaddatabase(self):
        # Using readline()
        file1 = open('data.txt', 'r')
        count = 0

        while True:
            count += 1
            line = file1.readline()

            if not line:
                break
            tempdata = line.split("|")

            if (re.findall("[a-z]", " ".join(tempdata[0].lower().split())) and tempdata[
                0] != ''):  # customerdata=[tempdata[1].lower().strip(),tempdata[2].lower().strip(),tempdata[3].lower().strip()]
                customerdata = [" ".join(tempdata[1].lower().split()), " ".join(tempdata[2].lower().split()),
                                " ".join(tempdata[3].lower().split())]
                self.customer[" ".join(tempdata[0].lower().split())] = customerdata

                # for temp in tempdata: # print(temp.lower().strip()) #print(" ".join(temp.lower().split())) # print("{}".format(line.strip()))
            elif (tempdata[0] == ''):
                print("database record is skipped")

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
