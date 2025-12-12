from socket import *

serverName="localhost"  
serverPort=80  # 80 for "gaia.cs.umass.edu"

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

# prepare the request to send. (use '\r\n' instead of '\n'!)
method = "GET"
filepath = "/index.html"  # /wireshark-labs/HTTP-wireshark-file1.html

request = f"{method} {filepath} HTTP/1.0\r\n\r\n"


clientSocket.send(request.encode())

clientSocket.settimeout(5)

http_response = bytearray()

try:
    while True:
        response = clientSocket.recv(4096)
        if not response:
            break
        http_response += response
        
except timeout:
    print("Socket time out.")


print(http_response.decode())

clientSocket.close()