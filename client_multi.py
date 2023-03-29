from socket import*
serverName = '192.168.197.18'
serverPort = 12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

def game1_chooser():
    close=0
    word=input()
    ans=['*']*len(word)
    count=0
    clientSocket.send(word.encode())
    print("Word sent to server")
    while(True):
        guess=""
        print("Waiting for guess...")
        guess=clientSocket.recv(2048).decode().upper()
        print("Guess=",guess)
        if("clue" in guess.lower()):
            print(guess)
            clue=input()
            clientSocket.send(clue.encode())
            continue
        flag=0
        pos=input("Enter the positions of occurances\n").split()
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
            print("Guessing done...")
            clientSocket.send(guess.encode())
            print("Guess sent to server")
            guess_res=clientSocket.recv(2048).decode()
            if("won" in guess_res.lower() or "lost" in guess_res.lower()):
                print(guess_res)
                clientSocket.close()
                break
            else:
                print(guess_res)
        if("clue" in mes.lower()):
            print(mes)

def game2():
    while(True):
        mes=clientSocket.recv(2048).decode()
        if(mes=="Play"):
            print(mes)
            inp=input()
            inp=inp.upper()
            while(inp!="ROCK" and inp!="PAPER" and inp!="SCISSOR"):
                inp=input("Choose between rock, paper or scissor\n").upper()
            clientSocket.send(inp.encode())
            rps_score=clientSocket.recv(2048).decode()
            if("won" in rps_score.lower() or "draw" in rps_score.lower()):
                print(rps_score)
                clientSocket.close()
                break
            else:
                print(rps_score)

while(True):
    print("Enter your choice(1 or 2)")
    choice=input()
    clientSocket.send(choice.encode())
    choice=clientSocket.recv(2048).decode()
    print(choice)
    if("hangman" in choice.lower()):
        if("choose" in choice.lower()):
            game1_chooser()
            break
        if("guess" in choice.lower()):
            game1_guesser()
            break
    if("rock" in choice.lower()):
        game2()
        break

