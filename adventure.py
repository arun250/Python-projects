name = input ("type your name")
print("welcome", name, "to this adventure")
answer = input("you are on a dirt road, it has come to an end and you can go left or right").lower()

if answer == "left":
    answer = input ("you come to a river, you can walk around it or swim across")
    
    if answer == "swim":
        print("you swam across and were eaten by an alligator")
    elif answer == "walk":
        print("you walked for many miles, ran out of water ans you lost the game")
    else:
        print("not a valid option. you lose")
        
elif answer == "right":
    answer = input ("you come to a bridge, it looks wobblyl do you want to cross it or head back (cross/back) ")
    
    if answer == "back":
        print("you go back and lose")
    elif answer == "cross":
        answer = input ("you cross the bridge and meet a stranger, Do you talk to the stranger ")

        if answer == "yes":
            print("you talk to a stranger, they give you gold. you win")
        elif answer == "no":
            print("you ignore the stranger and they are offended and you lost the game")
            
        else:
            print("not a valid option. you lose")
            



    else:
        print("not a valid option. you lose")
else:
    print("not a vaild option, you lose")

print("THank you for trying ", name)






