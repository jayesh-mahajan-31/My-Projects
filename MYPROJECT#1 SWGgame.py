#Snake Water Gun
import random
given=["Snake","Water","Gun"]
player1=0
computer=0
i=1
print("Lets Play!!")
while i<11:
    comp=random.choice(given)
    Player=input("S:Snake, W:Water, G:Gun,\n")
    if Player=="S" or Player=="W" or Player=="G":
        if Player==comp:
            print("No one Scores")
            print(comp)
        elif Player=="S" and comp=="Water":
            player1+=1
            print("Player Win", player1)
            print(comp)
        elif Player=="S" and comp=="Gun":
            computer+=1
            print("Computer Win", computer)
            print(comp)
        elif Player=="W" and comp=="Snake":
            computer+=1
            print("Computer Win", computer)
            print(comp)
        elif Player=="W" and comp=="Gun":
            player1+=1
            print("Player Win", player1)
            print(comp)
        elif Player=="G" and comp=="Water":
            computer+=1
            print("Computer Win", computer)
            print(comp)
        elif Player=="G" and comp=="Snake":
            player1+=1
            print("Player Win", player1)
            print(comp)
    else:
        print("Enter a Valid Choice.")
    i+=1
if player1>computer:
    print("Player WINS the SERIES.🥳🥳")
elif computer>player1:
    print("Computer WINS the SERIES.😅😅")
else:
    print("This was a TIE. No one wins.😐😐")
print("Computer = ",computer)
print("Player = ",player1)
