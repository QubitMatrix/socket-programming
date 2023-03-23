from socket import*
from count1 import *
serverName = '172.21.248.65'
serverPort = 12000
def games():
    while (True):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        def game1():
            while (True):
                message = input('Enter your guess:')
                clientSocket.send(message.encode())
                modMsg= clientSocket.recv(2048)
                # print(serverAddress)
                modMsg = modMsg.decode()
                if (modMsg == "end"):
                    break
                print(modMsg)

        def game2():
            print("Score format: You-Computer")
            while (True):
                message = get_count()
                message = str(message)
                clientSocket.send(message.encode())
                modMsg = clientSocket.recv(2048)
                modMsg = modMsg.decode()
                print(modMsg)
                if ("Game" in modMsg):
                    choice = input("end or no?")
                    clientSocket.send(choice.encode())
                    if (choice == "end"):
                        break

        choice = input("Enter the choice(1 or 2 or 3)")
        if (choice == '3'):
            break
        clientSocket.send(choice.encode())
        print("choice sent")
        while (True):  # waiting for acknowledgement before starting game
            modMsg= clientSocket.recv(2048)
            print("choice received")
            modMsg = modMsg.decode()
            print(modMsg)
            if ("scissor" in modMsg):
                game2()
                break
            if ("hangman" in modMsg):
                game1()
                break
    clientSocket.close()
games()
