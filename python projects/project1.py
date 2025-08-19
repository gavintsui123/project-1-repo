import random
import math

# name variables for the user and the computer
# assign numeric values to rock paper and scissors
# using conditionals to imitate scenarios

user_wins = 0
computer_wins = 0
options = ["rock" , "paper", "scissors"]
random_number = random.randint(0,2)


while True:
    user_input = input("Type either Rock,Paper,Scissors or q for quit ")
    if user_input == "q":
        break
    
    if user_input not in options:
        continue 

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "paper":
        print("You have won!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You have won!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You have won!")
        user_wins += 1
    
    print("you have won " +  str(user_wins) )
     
print("finished, bye")


    





    

