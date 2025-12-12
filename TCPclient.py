from socket import *

serverName=""  #
serverPort=2096  #

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

message = "Hello world, this is a message on the Internet."

clientSocket.send(message.encode())

recv_message = clientSocket.recv(1024)

print(recv_message.decode())

clientSocket.close()