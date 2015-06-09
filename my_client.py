import socket
import json
import argparse

ip = "localhost"
port = 8080

sock = socket.socket()

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="Ip to locate server on. Defaults to 'localhost'")
parser.add_argument("-p", "--port", type=int, help="Port to locate server on. Defaults to '8080'")
args = parser.parse_args()

class MyClient:

    def __init__(self):
        #create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        global ip
        global port

        if args.ip:
            ip = args.ip
        if args.port:
            port = args.port

        #define address of server
        server_address = (ip, port)

        print "Connecting to %s port %s" % server_address
        
        #connect to server
        sock.connect(server_address)

    def send(self, request):
        print "\nSending ", request
        sock.sendall(json.dumps(request))

        #get result back from server
        result = sock.recv(4096)

        print result

    def run(self):
        try:
            #test cases
            request = {"request":"cat"}
            self.send(request)

            request = {"request":"dog"}
            self.send(request)

            request = {"request":"bear"}
            self.send(request)

            request = {"invalid":"cat"}
            self.send(request)

            request = "Not json"
            self.send(request)

            #User Input
            while True:
                #take string input from user
                user_text = raw_input("Enter a request: ")
                if user_text == "":
                    break
                else:
                    #define request and send to server as json
                    request = {"request": user_text}
                    self.send(request)

        except SyntaxError, e:
            print "Client: Syntax Error"

        finally:
            #close socket
            sock.close()

def main():
    client = MyClient()
    client.connect()
    client.run()

if __name__ == "__main__":
    main()
