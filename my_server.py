import signal
import socket
import json
import argparse


class MyProtocol:

    #define function to check for contents of json
    def validate(self, json_data):
        #valid data for json to contain
        valid_data = ["cat", "dog", "bear"]

        #check if json contains valid data
        if json_data["request"] in valid_data:
            print "Valid request"
            print "Sending response back"
            return True
        else:
            print "Invalid request"
            print "Sending response back"
            return False

class MyServer:


    def __init__(self, sock):
        #Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def bind(self, args, sock):

        #define address for socket to be used on using arguments
        server_address = (args.ip, args.port)

        #print the address of the server
        print "Starting on %s port %s" % server_address

        #bind socket to address
        sock.bind(server_address)

    def run(self, sock):
        #start listening for conections, only allow 1 connection
        sock.listen(1)

        #Define protocol for use
        protocol = MyProtocol()

        while True:
            print "\nWaiting for a connection"
            try:
                #accept connections. conn is socket object, addr is address of client
                conn, addr = sock.accept()
            #if an error occurs, break out of the loop
            except socket.error:
                break

            try:
                #print the address of the connected client
                print "Connection from ", addr

                while True:
                    #receive data
                    data = conn.recv(4096)
                    #print the raw data that was received
                    print "\nReceived '%s' "% data
                    try:
                        #read data from json
                        json_data = json.loads(data)
                        if data:
                            #check for valid request
                            if protocol.validate(json_data):
                                #send back response as text
                                conn.sendall("Yes, you sent %s" % json_data["request"])

                            #if request is invalid
                            else:
                                #send back response as text
                                conn.sendall("No, you sent %s" % json_data["request"])
                        else:
                            print "No more data from ", addr
                            break
                    #Check for errors in json        
                    except ValueError, e:
                        print "Invalid Value"
                        #send error type as text to client
                        conn.sendall("Server: ValueError")
                    except KeyError, e:
                        print "Invalid Key"
                        #send error type as text to client
                        conn.sendall("Server: KeyError")
                    except TypeError, e:
                        print "Invalid Type"
                        #send error type as text to client
                        conn.sendall("Server: TypeError")

            #catch socket errors
            except socket.error:
                print "Socket Error"   

            finally:
                #close socket
                conn.close()

def main():

    #initialise a socket
    sock = socket.socket()

    #define argument parser
    parser = argparse.ArgumentParser()
    #add arguments to parser
    parser.add_argument("-i", "--ip", default="localhost", help="Ip to start server on. Defaults to 'localhost'")
    parser.add_argument("-p", "--port", type=int, default=8080, help="Port to start server on. Defaults to '8080'")
    args = parser.parse_args()

    #run functions in order
    serv = MyServer(sock)
    serv.bind(args, sock)
    serv.run(sock)

    #handle a signal interupt
    def signal_handler(signal, frame):
        print 'Ended'
        sock.close()


if __name__ == "__main__":
    main()
    signal.signal(signal.SIGINT, signal_handler)