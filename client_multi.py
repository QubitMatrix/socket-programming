from socket import*
serverName = '192.168.85.1'
serverPort = 12000
print("a")
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print("b")
def game1_chooser():
    close=0
    word=input()
    ans=['*']*len(word)
    count=0
    clientSocket.send(word.encode())
    print("word sent")
    while(True):
        guess=""
        print("waiting for guess")
        guess=clientSocket.recv(2048).decode().upper()
        print("guess=",guess)
        if("clue" in guess.lower()):
            print(guess)
            clue=input()
            clientSocket.send(clue.encode())
            continue
        flag=0
        pos=input("Enter the positions of occurances").split()
        if('-1' not in pos):
            for x in range(len(pos)):
                ans[int(pos[x])-1]=guess
                flag=1
        if(flag==0):
            count+=1
        if(count==7 and '*' in ans):
            mes="You lost...The word is "+word+":"+str(count)
            close=1
        elif(count<7 and '*' not in ans):
            mes="You won...The word is "+word+":"+str(count)
            close=1
        else:
            mes="".join(ans)+":"+str(count)
        clientSocket.send(mes.encode())
        if(close):
            break

def game1_guesser():
    while(True):
        mes=clientSocket.recv(2048).decode()
        if("Enter" in mes):
            guess=input(mes)
            print("Guess done")
            clientSocket.send(guess.encode())
            print("Guess sent")
            guess_res=clientSocket.recv(2048).decode()
            if("won" in guess_res.lower() or "lost" in guess_res.lower()):
                print(guess_res)
                clientSocket.close()
                break
            else:
                print(guess_res)
        if("clue" in mes.lower()):
            print(mes)

while(True):
    print("Enter your choice(1 or 2 or 3)")
    choice=input()
    print("a")
    clientSocket.send(choice.encode())
    print("b")
    choice=clientSocket.recv(2048).decode()
    print(choice)
    if("hangman" in choice.lower()):
        if("choose" in choice.lower()):
            game1_chooser()
            break
        if("guess" in choice.lower()):
            game1_guesser()
            break
#clientSocket.close()
