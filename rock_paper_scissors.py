import random
#this is giving the available choices for the computer to use.
computer_choice = random.choice(["scissors", "rock", "paper"])

user_choice = input("Do you want - rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "scissors":
    print("you WIN")
elif user_choice == "paper" and computer_choice == "rock":
    print("you WIN")
elif user_choice == "scissors" and computer_choice == "paper":
    print("you WIN")
else:
    print("you LOSE")