import random
names=open("words.txt",'r')
names=names.readlines()
a=random.randrange(10)
word=names[a]
word=word.strip()
ans_space=['*']*len(word)
def hangman_fun(inp,count):
    global ans_space
    global word
    word=word.upper()
    flag=0
    for x in range(len(ans_space)):
        if(inp==word[x]):
            flag=1
            ans_space[x]=inp
    if(flag==0):
        count+=1
    print("in hangman.py",ans_space,count)
    if('*' not in ans_space and count<=7):
        return ("You won. The word is "+"".join(ans_space),count)
    if(count==7 and '*' in ans_space):
        return ("You lose",count)
    return (ans_space,count)
