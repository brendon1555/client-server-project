import socket
import json
import argparse


class MyClient:

    def __init__(self, sock):
        #create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, args, sock):

        #define address of server
        server_address = (args.ip, args.port)

        #print address of server
        print "Connecting to %s port %s" % server_address

        #connect to server
        sock.connect(server_address)

    def send(self, request, sock):
        #print the request being sent
        print "\nSending ", request
        #send the request
        sock.sendall(json.dumps(request))

        #get result back from server
        result = sock.recv(4096)

        #print the returned result
        print result

    def run(self, sock):
        try:
            #test cases
            #define the request
            request = {"request":"cat"}
            #call send function to send request
            self.send(request, sock)

            request = {"request":"dog"}
            self.send(request, sock)

            request = {"request":"bear"}
            self.send(request, sock)

            request = {"invalid":"cat"}
            self.send(request, sock)

            request = "Not json"
            self.send(request, sock)

            #User Input
            while True:
                #take string input from user
                user_text = raw_input("Enter a request: ")
                #if the user doesnt enter anything, break out of loop
                if user_text == "":
                    break
                else:
                    #define the request
                    request = {"request": user_text}
                    #call send function to send request
                    self.send(request, sock)
        #catch syntax errors
        except SyntaxError, e:
            print "Client: Syntax Error"

        finally:
            #close socket
            sock.close()

def main():

    #initialise a socket
    sock = socket.socket()

    #define argument parser
    parser = argparse.ArgumentParser()
    #add arguments to parser
    parser.add_argument("-i", "--ip", default="localhost", help="Ip to locate server on. Defaults to 'localhost'")
    parser.add_argument("-p", "--port", type=int, default=8080, help="Port to locate server on. Defaults to '8080'")
    args = parser.parse_args()

    #run functions in order
    client = MyClient(sock)
    client.connect(args, sock)
    client.run(sock)

    #handle a signal interupt
    def signal_handler(signal, frame):
        print 'Ended'
        sock.close()

if __name__ == "__main__":
    main()
    signal.signal(signal.SIGINT, signal_handler)