# """_1. input from me
# 3. result print
# case..///
# (a) rock   
#              rock-rock=tie
#              rock-paper=paper wins
#              rock-scissor=rock wins
# (b) paper  
#            paper-paper=tie
#            paper-rock=paper wins
#            paper-scissor=scissor wins
# (C) scissor   
#               sci-sci=tie
#               sci-paper=sci wins
#               sci-rock=rock wins
    
import random
item_list=["Rock","paper","scissor"]
user_choice=input("enter your move=rock,paper,scissor==")
comp_choice=random.choice(item_list)
print(f"user choice ={user_choice}, Computer choice={comp_choice}")

if user_choice==comp_choice:
    print("both choose same so match tie!!")
elif user_choice=="rock":
    if comp_choice=="paper":
        print("paper covers rock so ==computer wins!!")
    else:
        if comp_choice=="scissor":
           print("rock breaks scissor==Rock wins!!u  win")
elif user_choice=="paper":
    if comp_choice=="scissor":
        print("scissor cuts paper so==computer wins!!")
    else:
        print("paper covers rock so==You win!!")
elif user_choice=="scissor":
    if comp_choice=="paper":
        print("scissor can cut paper so== you Win!!")
    else:
        print("rock breaks scissor so== computer wins!!")
else:
    print("invalid choice ..you can only type rock,paper ,scissor!!!")