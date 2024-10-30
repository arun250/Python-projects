import random

def roll():
    min_value  = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4)")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
    else:
        print("must between 2 and 4")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores)< max_score:
    for player_idx in range(players):
        print("player number",player_idx +1, "turn has jzst started")
        print("your totla score is ", player_scores[player_idx])
        
        
        while True:
            current_score =0 
            should_roll = input("would you like to roll (y)?")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("you rolled a 1! turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled a:", value)
            
            print("your score is ", current_score)
        
        player_scores[player_idx] += current_score
        print("your totla score is ", player_scores[player_idx])
        
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

print("plaxer numbner", winning_idx+1, "is the winner with a score of ", max_score)

