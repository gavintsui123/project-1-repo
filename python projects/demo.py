#rock paper scissors game
import random
import math

user_wins = 0 
computer_wins = 0
options = ["Rock ","Paper ", "Scissors "]
random_number = random.randint(0,2)
# index rock = 0 paper = 1 scissors = 2


while True: 
    user_input = input("Type either rock, paper, scissors or q for quit ")
    if user_input == "q":
        print("You have quit the game")
        break
    
    if user_input in options:
        continue 

    computer_pick = options[random_number]
    print("Computer has picked ", computer_pick + ".")
        
    if user_input == "rock" and computer_pick == "paper":
        print("you have won!")
        user_input += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("you have won!")
        user_input += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("you have won!")
        user_input += 1

    print("you have won", user_wins)

print("Finished, bye! ")
  

    
