import random
computer=random.choice([-1,0,1])
youstr=input("enter your choice:")
youDict={"s":1,"w":0,"g":-1}
reverseDict= {1:"snake",0:"water",-1:"gun"}
you=youDict[youstr]
print(f"you chose{reverseDict[you]}\ncomputer chose{reverseDict[computer]}")
if(computer==you):
    print("its a draw")

else:
    if(computer==-1 and you==1):
        print("you win")
    if(computer==-1 and you==0):
        print("you win")
    if(computer==1 and you==-1):
        print("you win")
    if(computer==1 and you==0):
        print("you win")
    if(computer==0 and you==-1):
        print("you win")
    if(computer==0 and you==1):
        print("you win")
    