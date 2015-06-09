import socket
import json

#create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define address of server
server_address = ("localhost", 8080)

print "Connecting to %s port %s" % server_address
#connect to server
sock.connect(server_address)

try:
    #take string input from user
    user_text = raw_input("Enter a request: ")

    #define request and send to server as json
    request = {"request": user_text}
    print "Sending ", request
    sock.sendall(json.dumps(request))
    #get result back from server
    result = sock.recv(1024)

    print result


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

except SyntaxError, e:
    print "Client: Syntax Error"

finally:
    #close socket
    sock.close()