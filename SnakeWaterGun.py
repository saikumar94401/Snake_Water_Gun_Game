import random
game=["Snake","Water","Gun"]
comp=0
user=0
atempts=10
draw=0
print("Game Starts now..............")
while(atempts>0):
    computer =random.choice(game)
    print("Enter:s for Snake||w for water||g for gun")
    choice=input("Enter your choice")
    if choice=='s'or choice =='S':
        if computer=="Water":
            user+=1
            print("User Won")
        elif computer=="Gun":
            comp+=1
            print("Computer Won")
        else:
            print("Draw")
            draw+=1
        atempts -= 1
    elif choice=='w' or choice=='W':
        if computer=="Snake":
            comp+=1
            print("Computer Won")
        elif computer=="Gun":
            user+=1
            print("User Won")
        else:
            print("Draw")
            draw += 1
        atempts -= 1
    elif choice=='g'or choice=='G':
        if computer=="Water":
            user+=1
            print("User Won")
        elif computer=="Snake":
            comp+=1
            print("Computer Won")
        else:
            print("Draw")
            draw += 1
        atempts -= 1
    else:
        print("invalid input")

print("Game over")
print("User Score",user)
print("Computer Score",comp)
if draw>0:
    print("Draw",draw)
if user>comp:
    print("You Won")
elif user<comp:
    print("Computer Won")
else:
    print("Draw Match")

