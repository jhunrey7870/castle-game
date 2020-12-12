import random
print("You are stuck inside a dark room inside a weird af castle that somehow u got inside")
print("Theres also 4 doors, you have to choose one that can help you gtfo")
playerChoice = input("Choose 1,2,3 or 4:")
if playerChoice == "1":
    print("nah ur dead for no reason, start again chod")
    print("You have lost the game!")
elif playerChoice == "2": 
    print("The door opens slightly, a giant angrily jumps out and bashed on you with a baseball bat")
    print("You have lost the game!")
elif playerChoice == "3":
    print("You've entered the room and saw a sleeping, fatass dragon just like ping")
    print("You can either choose:")
    print("1. Steal the dragon's expensive s20 ultra")
    print("2. Carefully go pass the dragon")
    print("Select your life decision:)
    dragonChoice = input("Choose 1 or 2")
    if dragonChoice == "1":
        print("Nah too bad, the dragon noticed his aod went off and he ate you alongside your j7 2016")
        print("You have lost the game!")
    elif dragonChoice == "2":
        print("You have carefully went pass the dragon!")
        print("You have beaten the game! Congratulations!!")
    else:
        print("u idiot select one or two lmao")
else:
    print("Too bad, try again, you have not selected 1 or 2 or 3 or 4 at all =/")
print("Restart the game to enjoy the adventure again!")
