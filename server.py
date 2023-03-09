from socket import *
from hangman import *
serverPort=12002
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("Server ready")
count=0
while True:
    message,clientAddress=serverSocket.recvfrom(2048)
    print(clientAddress)
    modMsg=message.decode().upper()
    ans,count=hangman_fun(modMsg,count)
    ans="".join(ans)
    print("in server",ans,count)
    serverSocket.sendto(ans.encode(),clientAddress)
