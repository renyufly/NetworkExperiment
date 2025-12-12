from socket import *
import os

serverName="localhost"  

serverPort = 80   # 

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverName, serverPort))

webDirectory = "./web"

serverSocket.listen(1)
print(f"======The server starts at port{serverPort}=====")

while True:
    clientSocket, addr = serverSocket.accept()

    # receive the HTTP request and parse it
    request = clientSocket.recv(4096).decode()

    print(f"received: {request}")
    
    # GET
    method = request.split()[0]

    print(f"method: {method}")

    # /xxx.html -> xxx.html
    request_uri = request.split()[1][1:]

    print(f"request_uri: {request_uri}")

    request_uri = os.path.join(webDirectory, request_uri.lstrip("/"))

    msg = str()

    # generate HTTP response to send back
    if method.strip() == "GET":
        # msg = (f"HTTP/1.1 200 OK\r\n"
        #        f"\r\n\r\n"
        #        f"<html>Hello World</html>") 
        if os.path.exists(request_uri):
            msg = (f"HTTP/1.1 200 OK\r\n"
                   f"Content-Length: {str(os.path.getsize(request_uri))}\r\n\r\n"
                   + open(request_uri, "r").read()) 
                    # f"<html>Hello World</html>"
        else:
            msg = (f"HTTP/1.1 404 Not Found\r\n")
            
    clientSocket.send(msg.encode())

    clientSocket.close()

