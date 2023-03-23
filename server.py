from socket import *
from hangman import *
from sps import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Server ready")
def game1(connectionSocket,clientAddress):
    count=0
    word,hint=choose_word()
    ans=""
    print("hangman",clientAddress)
    connectionSocket.send("Get ready to play hangman!!!".encode())
    while True:
        message=connectionSocket.recv(2048)
        print(clientAddress)
        if("You won" in ans or "You lose" in ans):
          word,hint=choose_word()
        modMsg=message.decode().upper()
        if(modMsg.lower()=="end"):
          connectionSocket.send(modMsg.lower().encode())
          connectionSocket.close()
          break
        ans,count=hangman_fun(word,hint,modMsg,count)
        ans="".join(ans)
        print("in server",ans,count)
        connectionSocket.send(ans.encode())
def game2(connectionSocket,clientAddress):
    count=0
    comp=0
    player=0
    player_choice=""
    counter=0
    print("SPS")
    connectionSocket.send("Get ready to play stone,paper,scissor".encode())
    while True:
        count=connectionSocket.recv(2048)
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
        if(counter==3):
            counter=0
            if (player==comp):
                winner="Draw"
            else:
                winner="You won" if player>comp else "Computer won"
            comp=0
            player=0
            ans=ans+"\nGame over..."+winner
            connectionSocket.send(ans.encode())
            msg=connectionSocket.recv(2048)
            if(msg.decode().lower()=='end'):
                connectionSocket.close()
                break
        else:
            connectionSocket.send(ans.encode())
while(True): #to choose which game
    connectionSocket,clientAddress=serverSocket.accept()
    choice=connectionSocket.recv(2048)
    choice=choice.decode()
    print(choice)
    if(choice=='1'):
        game1(connectionSocket,clientAddress)
    elif (choice=='2'):
        game2(connectionSocket,clientAddress)
    choice=0
    #connectionSocket.close()
