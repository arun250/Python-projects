print("Welcome to my computer quiz!")
playing = input("Do you want to play")

if playing.lower() != "yes":
    quit()
    
print("Okay! Lets play:)")
score = 0

answer = input("what does CPU stands for")
if answer == "Central Processing Unit":
    print("COrrect!")
    score +=1
else:
    print("Incorrect!!")

answer = input("what does GPU stands for")
if answer == "Graphics Processing Unit":
    print("COrrect!")
    score +=1
else:
    print("Incorrect!!")

answer = input("what does RAM stands for")
if answer == "Random Access Memory":
    print("COrrect!")
    score +=1
else:
    print("Incorrect!!")

answer = input("what does PSU stands for")
if answer == "Power Supply":
    print("Correct!")
    score +=1
else:
    print("Incorrect!!")

print("you got" + str(score) + "Questions correct")
print("you got" + str((score)/4 * 100 ) + "%.")

