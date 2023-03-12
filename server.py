from socket import *
from hangman import *
from sps import *
serverPort=12002
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("Server ready")
def game1(clientAddress):
    count=0
    word,hint=choose_word()
    ans=""
    print("hangman",clientAddress)
    serverSocket.sendto("Get ready to play hangman!!!".encode(),clientAddress)
    while True:
        message,clientAddress=serverSocket.recvfrom(2048)
        print(clientAddress)
        if("You won" in ans or "You lose" in ans):
          word,hint=choose_word()
        modMsg=message.decode().upper()
        if(modMsg.lower()=="end"):
          serverSocket.sendto(modMsg.lower().encode(),clientAddress)
          break
        ans,count=hangman_fun(word,hint,modMsg,count)
        ans="".join(ans)
        print("in server",ans,count)
        serverSocket.sendto(ans.encode(),clientAddress)
def game2(clientAddress):
    count=0
    comp=0
    player=0
    player_choice=""
    counter=0
    print("SPS")
    serverSocket.sendto("Get ready to play stone,paper,scissor".encode(),clientAddress)
    while True:
        count,clientAddress=serverSocket.recvfrom(2048)
        count=count.decode()
        print(count)
        count=int(count)
        if(count==0):
            player_choice="stone"
        if(count==2):
            player_choice="scissor"
        if(count==5):
            player_choice="paper"
        ans,comp_choice=sps_fun(count)
        if(ans==1):
            player+=1
        if(ans==2):
            comp+=1
        print("in server",player,count,comp,comp_choice)
        ans="Score:"+str(player)+"-"+str(comp)+"\n("+player_choice+","+comp_choice+")"
        counter+=1
        if(counter==7):
            counter=0
            if (player==comp):
                winner="Draw"
            else:
                winner="You won" if player>comp else "Computer won"
            comp=0
            player=0
            ans=ans+"\nGame over..."+winner
            serverSocket.sendto(ans.encode(),clientAddress)
            msg,clientAddress=serverSocket.recvfrom(2048)
            if(msg.decode().lower()=='end'):
                break
        else:
            serverSocket.sendto(ans.encode(),clientAddress)
while(True): #to choose which game
    choice,clientAddress=serverSocket.recvfrom(2048)
    choice=choice.decode()
    print(choice)
    if(choice=='1'):
        game1(clientAddress)
    elif (choice=='2'):
        game2(clientAddress)
    choice=0
