import socket
import json
import argparse


ip = "localhost"
port = 8080

sock = socket.socket()

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="Ip to start server on.")
parser.add_argument("-p", "--port", type=int, help="Port to start server on.")
args = parser.parse_args()

class MyServer:

    def __init__(self):

        #Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def bind(self):
        global ip
        global port
        
        if args.ip:
            ip = args.ip
        if args.port:
            port = args.port

        #define address for socket to be used on
        server_address = (ip, port)

        print "Starting on %s port %s" % server_address

        #bind socket to address
        sock.bind(server_address)


    def run(self):
        #start listening for conections, only allow 1 connection
        sock.listen(1)
        while True:
            print "\nWaiting for a connection"
            #accept connections. conn is socket object, addr is address of client
            conn, addr = sock.accept()

            try:
                print "Connection from ", addr

                while True:
                    #receive data
                    data = conn.recv(1024)
                    print "\nReceived '%s' "% data
                    try:
                        #read data from json
                        json_data = json.loads(data)
                        if data:
                            #check for valid request
                            if (json_data["request"] == "cat") or (json_data["request"] == "dog") or (json_data["request"] == "bear"):
                                print "Valid request"
                                print "Sending response back"
                                #send back response as text
                                conn.sendall("Yes, you sent %s" % json_data["request"])
                            #if request is invalid
                            else:
                                print "Invalid request"
                                print "Sending response back"
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
    serv = MyServer()
    serv.bind()
    serv.run()

if __name__ == "__main__":
    main()
