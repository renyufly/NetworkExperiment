from socket import *

serverPort = 2096

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", serverPort))

serverSocket.listen(1)
print("======The server is ready=====")

while True:
    connectionSocket, addr = serverSocket.accept()

    msg = connectionSocket.recv(1024).decode()
    print(f"server receives: {msg}")
    connectionSocket.send(msg.encode())

    connectionSocket.close()
