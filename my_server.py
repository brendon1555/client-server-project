import socket

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
            data = conn.recv(16)
            print "Received '%s'" % data
            if data:
                print "Sending data back"
                conn.sendall(data)
            else:
                print "No more data from ", addr
                break
    finally:
        conn.close()