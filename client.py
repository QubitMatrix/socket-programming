from socket import*
from count1 import *
serverName='172.21.248.65'
serverPort=12002
clientSocket=socket(AF_INET,SOCK_DGRAM)
while(True):
    def game1():
        while (True):
            message = input('Enter your guess:')
            clientSocket.sendto(message.encode(), (serverName, serverPort))
            modMsg, serverAddress = clientSocket.recvfrom(2048)
            # print(serverAddress)
            modMsg = modMsg.decode()
            if (modMsg == "end"):
                break
            print(modMsg)
    def game2():
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
                choice=input("end or no?")
                clientSocket.sendto(choice.encode(),(serverName,serverPort))
                if(choice=="end"):
                    break


    choice = input("Enter the choice(1 or 2 or 3)")
    if (choice == '3'):
        break
    clientSocket.sendto(choice.encode(), (serverName, serverPort))
    while (True):  # waiting for acknowledgement before starting game
        modMsg, serverAddress = clientSocket.recvfrom(2048)
        modMsg = modMsg.decode()
        print(modMsg)
        if ("scissor" in modMsg):
            game2()
            break
        if ("hangman" in modMsg):
            game1()
            break
clientSocket.close()
