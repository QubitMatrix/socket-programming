from socket import *
from sps import *
serverPort=12002
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("Server ready")
count=0
comp=0
player=0
player_choice=""
counter=0
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
    else:
        serverSocket.sendto(ans.encode(),clientAddress)
