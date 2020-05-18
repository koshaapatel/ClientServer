import socketserver
import re

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # print(database.customer.keys())
        # print(database.customer.values())
        # self.request is the TCP socket connected to the client
        while True:
            self.data = self.request.recv(1024).strip()
            if not self.data:
                print("exit")
                break
            # print("{} wrote:".format(self.client_address[1]))
            print("{} wrote:".format(self.client_address[0]))
            # received = self.data.decode("utf-8")
            received = str(self.data, "utf-8")
            print("Received: {}".format(received))
            # just send back the same data, but upper-cased
            self.request.sendall(bytes(received.upper() + "\n", "utf-8"))
            print("Sent:     {}".format(received.upper()))

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
            # Get next line from file
            line = file1.readline()

            # if line is empty
            # end of file is reached
            if not line:
                break
            tempdata = line.split("|")

            if (re.findall("[a-z]", " ".join(tempdata[0].lower().split())) and tempdata[0] != ''):
                # customerdata=[tempdata[1].lower().strip(),tempdata[2].lower().strip(),tempdata[3].lower().strip()]
                customerdata = [" ".join(tempdata[1].lower().split()), " ".join(tempdata[2].lower().split()),
                                " ".join(tempdata[3].lower().split())]
                self.customer[" ".join(tempdata[0].lower().split())] = customerdata

                for temp in tempdata:
                    # print(temp.lower().strip())
                    print(" ".join(temp.lower().split()))
                    # print("{}".format(line.strip()))
            elif(tempdata[0] == ''):
                print("database record is skipped")

        file1.close()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    database=SingletonDatabase()
    database.loaddatabase()

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as serversocket:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        serversocket.serve_forever()
        serversocket.server_close()