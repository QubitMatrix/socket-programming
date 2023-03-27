from socket import *
import os
from _thread import *
serverSocket=socket(AF_INET,SOCK_STREAM)
serverName=""
serverPort=12000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
chooser=""
guesser=""
guess_message=""
guess_ans=""
guessed=0
checked=1
thread=0
break_=0
print("Server ready")
def game1_guesser(clientAddress):
    global guess_message
    global guessed
    global checked
    while(True):
        if(break_):
            break
        if(checked):
            guesser.send("Enter your guess".encode())
            print("Enter the guess")
            guess_message=guesser.recv(2048).decode().upper()
            print("guess_message",guess_message)
            chooser.send(guess_message.encode())#a
            print("guess sent")
        if(guess_message!=""):
            guessed=1
            checked=0
            guess_message=""
def game1_chooser(clientAddress,word):
    global guess_ans
    global guessed
    global checked
    global break_
    clue=0
    while(True):
        print("x")
        guess_ans=chooser.recv(2048).decode().upper()#**a**r(or win/lose),count
        if(not guess_ans):
            continue
        print("Got guess ans")
        guess_ans,count=guess_ans.split(":")
        guesser.send(guess_ans.encode())
        print("sent guess aswner",count)
        if(count=="-1"):
            break_=1
            break
        if(count=="3" and clue==0):
            clue=1
            chooser.send("Enter the clue".encode())
            clue="Clue="+chooser.recv(2048).decode().upper()
            print("clue",clue)
            guesser.send(clue.encode())
        if(guess_ans!=""):
            guessed=0
            checked=1
            guess_ans=""

def pre_game1(clientSocket,clientAddress):
    global chooser
    global guesser
    print("hangman")
    while(True):
        if(chooser==""):
            mes="Get ready to play hangman\nChoose a word\n"
            print(mes)
            chooser=clientSocket
            clientSocket.send(mes.encode())
            print("a")
            word=chooser.recv(2048).decode().upper()
            print(word)
            game1_chooser(clientAddress,word)
            break
        else:
            mes="Get ready to play hangman\nYou will be guessing the  word\n"
            guesser=clientSocket
            clientSocket.send(mes.encode())
            print("idc")
            game1_guesser(clientAddress)
            break

def multi_client(clientSocket,clientAddress):
    while(True):
        choice=clientSocket.recv(2048).decode()
        print(clientAddress,"chose",choice)
        if(choice=='1'):
            pre_game1(clientSocket,clientAddress)
            break
        elif(choice=='2'):
            game2(clientSocket,clientAddress)
            break
        choice=0
        
while(True):
    connectionSocket,clientAddress=serverSocket.accept()
    print("Connected to: "+clientAddress[0])
    start_new_thread(multi_client,(connectionSocket,clientAddress,))
    thread+=1
    print("Clients connected: ",thread);
serverSocket.close()
