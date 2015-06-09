import socket
import json

#Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define address for socket to be used on
server_address = ('localhost', 8080)

print "Starting on %s port %s" % server_address

#bind socket to address
sock.bind(server_address)

#start listening for conections, only allow 1 connection
sock.listen(1)


while True:
    print "Waiting for a connection"
    #accept connections. conn is socket object, addr is address of client
    conn, addr = sock.accept()

    try:
        print "Connection from ", addr

        while True:
            data = conn.recv(1024)
            print "Received '%s'" % data
            try:
                json_data = json.loads(data)
                if data:
                    if (json_data["request"] == "cat") or (json_data["request"] == "dog") or (json_data["request"] == "bear"):
                        print "Valid request"
                        print "Sending response back"
                        conn.sendall("Yes, you sent %s" % json_data["request"])
                    else:
                        print "Invalid request"
                        print "Sending response back"
                        conn.sendall("No, you sent %s" % json_data["request"])
                else:
                    print "No more data from ", addr
                    break
            except ValueError, e:
                print "Invalid Value"
                conn.sendall("ValueError")

            except KeyError, e:
                print "Invalid Key"
                conn.sendall("KeyError")

            except TypeError, e:
                print "Invalid Type"
                conn.sendall("TypeError")
    finally:
        conn.close()