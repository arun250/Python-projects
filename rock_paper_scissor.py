import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]
while True:
    user_input = input("Enter Rock/Paper/Scissors or Q to Quit").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")
    if computer_pick == "scissors" and user_input== "rock" :
        print("you won!")
        user_wins +=1
        
    elif computer_pick == "rock" and user_input== "paper" :
        print("you won!")
        user_wins +=1
        
    elif computer_pick == "paper" and user_input== "scissors" :
        print("you won!")
        user_wins +=1
        
    else:
        print("Computer wins")
        computer_wins +=1
print("you won", user_wins, "times")
print("computer won", computer_wins, "times")
print("Good bye")
            