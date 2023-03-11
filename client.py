from socket import*
serverName='172.20.117.235'
serverPort=12002
clientSocket=socket(AF_INET,SOCK_DGRAM)
while(True):
    message=input('Enter your guess:')
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    modMsg,serverAddress=clientSocket.recvfrom(2048)
    #print(serverAddress)
    modMsg=modMsg.decode()
    if(modMsg=="end"):
        break
    print(modMsg)
clientSocket.close()

