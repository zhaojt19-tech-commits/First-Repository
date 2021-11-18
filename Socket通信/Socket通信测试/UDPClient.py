from socket import *

serverName = "183.173.108.56"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = 'hello world'
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
print(serverAddress)
clientSocket.close()
