import random
r=random.randint(1,3)
win =False
def game():
    pass
print ("Computer thinking:stone(s) paper(p) or scissors(sc) ")
if r==1:
    comp="stone"
elif r==2:
    comp="paper"
elif r==3:
    comp="scissors"
b=str(input("player turn:stone(1) paper(2) or scissors(3)? "))
print ("computer choosed",comp)
if b =="stone" and comp=='sc':
    win = True 
elif b=="paper" and comp=="s":
    win=True
elif b=="scissors" and comp=="p":
    win=True

if b =="stone" and comp=="p":
    win = False 
elif b=="paper" and comp=="sc":
    win=False
elif b=="scissors" and comp=="s":
    win=False
elif win==True:
    print ("the player won!")
elif win ==False:
    print("computer won!")


