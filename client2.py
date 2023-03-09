from socket import*
from count1 import *
serverName='172.21.248.65'
serverPort=12002
clientSocket=socket(AF_INET,SOCK_DGRAM)
print("Score format: You-Computer")
while(True):
    message=get_count()
    message=str(message)
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    modMsg,serverAddress=clientSocket.recvfrom(2048)
    print(serverAddress)
    modMsg=modMsg.decode()
    print(modMsg)
    if("Game" in modMsg):
        break
clientSocket.close()

