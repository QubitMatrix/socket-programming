import random
def choose_word():
    global w
    global h
    global ans_space
    names=open("words.txt",'r')
    names=names.readlines()
    a=random.randrange(10)
    k=names[a].split(',')
    w=k[0]
    h=k[1]
    w=w.strip()
    h=h.strip()
    ans_space=['*']*len(w)
    return (w,h)
def hangman_fun(word,hint,inp,count):
    global ans_space
    print(word,hint)
    word=word.upper()
    flag=0
    for x in range(len(ans_space)):
        if(inp==word[x]):
            flag=1
            ans_space[x]=inp
    if(flag==0):
        count+=1
    if(count==3 and flag==0):
      return("HINT:"+hint,count)
    print("in hangman.py",ans_space,count)
    if('*' not in ans_space and count<=7):
      count=0
      return ("You won. The word is "+"".join(ans_space),count)
    if(count==7 and '*' in ans_space):
      count=0
      return ("You lose",count)
    return (ans_space,count)
