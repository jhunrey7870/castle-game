import random
exitChoice = "jhunrey is gay lmao"
while exitChoice != "ping is handsome":
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
    dragonChoice = input("Select your life decision:")
    if dragonChoice == "1":
        print("Nah too bad, the dragon noticed his aod went off and he ate you alongside your j7 2016")
        print("You have lost the game!")
    elif dragonChoice == "2":
        print("You have carefully went pass the dragon!")
        print("You have beaten the game! Congratulations!!")
    else:
        print("u idiot select one or two lmao")
elif playerChoice == "4":
    print("You have entered a room and theres a witch, he has a random number from 1 to 5, try to guess what is it")
    number = int(input("Choose your number:"))
    if number == random.randint(1,5):
        print("The witch was sad and feel ashamed because you guessed right! He drank some H2SO4 and dissolved!")
        print("You have won the game!")
    else:
        print("Too bad, your answer is incorrect and now you have to become the witch's slave for the rest of your life!")
        print("You have lost the game, try again!")
else:
    print("Too bad, try again, you have not selected 1 or 2 or 3 or 4 at all =/")
    exitChoice = input("Press enter to restart the game and enjoy the adventure again! (press space and enter to exit)")
