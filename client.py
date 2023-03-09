from socket import*
serverName='172.21.248.65'
serverPort=12002
clientSocket=socket(AF_INET,SOCK_DGRAM)
while(True):
    message=input('Enter your guess:')
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    modMsg,serverAddress=clientSocket.recvfrom(2048)
    print(serverAddress)
    modMsg=modMsg.decode()
    print(modMsg)
    if(modMsg=="You lose" or "You won" in modMsg):
        break
clientSocket.close()

