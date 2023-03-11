from socket import *
from hangman import *
serverPort=12002
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("Server ready")
count=0
word,hint=choose_word()
ans=""
while True:
    message,clientAddress=serverSocket.recvfrom(2048)
    print(clientAddress)
    if("You won" in ans or "You lose" in ans):
      word,hint=choose_word()
    modMsg=message.decode().upper()
    if(modMsg.lower()=="end"):
      serverSocket.sendto(modMsg.lower().encode(),clientAddress)
    ans,count=hangman_fun(word,hint,modMsg,count)
    ans="".join(ans)
    print("in server",ans,count)
    serverSocket.sendto(ans.encode(),clientAddress)