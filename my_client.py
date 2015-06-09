import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 8080)

print "Connecting to %s port %s" % server_address

sock.connect(server_address)

try:

    request = {"request":"cat"}
    print "Sending ", request
    sock.sendall(json.dumps(request))
    result = sock.recv(1024)

    print result


    request = {"request":"dog"}
    print "Sending ", request
    sock.sendall(json.dumps(request))
    result = sock.recv(1024)

    print result


    request = {"request":"bear"}
    print "Sending ", request
    sock.sendall(json.dumps(request))
    result = sock.recv(1024)

    print result


    request = {"invalid":"cat"}
    print "Sending ", request
    sock.sendall(json.dumps(request))
    result = sock.recv(1024)

    print result

    request = "Not json"
    print "Sending ", request
    sock.sendall(json.dumps(request))
    result = sock.recv(1024)

    print result

finally:
    sock.close()