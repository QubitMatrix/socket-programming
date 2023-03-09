import random
def sps_fun(n):
    n=int(n)
    a=random.randrange(3)
    print("a",a)
    if(n==0):
        if(a==0):
            return ((0,"Stone"))
        elif(a==1):
            return((2,"Paper"))
        else:
            return((1,"Scissor"))
    if(n==2):
        if (a == 0):
            return((2,"Stone"))
        elif (a == 1):
            return((1,"Paper"))
        else:
            return((0,"Scissor"))
    if(n==5):
        if (a == 0):
            return((1,"Stone"))
        elif (a == 1):
            return ((0,"Paper"))
        else:
            return((2,"Scissor"))
