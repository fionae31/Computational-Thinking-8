# Beginning: create variables
lorelai_points = 0
rory_points = 0
emily_points = 0


#Middle: Ask questions
answer = input ("In your free time would you rather A) read a good book, B) go to a waterpark, or C) gossip about sophisticated friends?")
if answer == "A":
    rory_points += 1
elif answer == "B":
    lorelai_points += 1
elif answer == "C":
    emily_points += 1


answer = input ("Are you A) God in the form of Britney Spears, B) a chill guy, or C) pearls and velvet?")
if answer == "A":
    lorelai_points += 1
elif answer == "B":
    rory_points += 1
elif answer == "C":
    emily_points += 1


answer = input ("Should your living quarters be A) a brick london flat, B) a colorful treehouse, or C) an elegant manor?")
if answer == "A":
    rory_points += 1
elif answer == "B":
    lorelai_points += 1
elif answer == "C":
    emily_points += 1


answer = input ("Would you name your dog A) rufus, B) bentley archibald the third, or C) paul")
if answer == "A":
    rory_points += 1
elif answer == "B":
    emily_points += 1
elif answer == "C":
    lorelai_points += 1


answer = input ("If faced with a personal issue, do you A) joke about it, B) deflect the problem onto others, or C) try to figure out how you feel about the issue?")
if answer == "A":
    lorelai_points += 1
elif answer == "B":
    emily_points += 1
elif answer == "C":
    rory_points += 1

answer = input ("A) My book looks sad, can a book look sad? B) Oy, with the poodles already, C) Ah, how Mcdonald's of you")
if answer == "A":
    rory_points += 1
elif answer == "B":
    lorelai_points += 1
elif answer == "c":
    emily_points += 1

answer = input ("Would you rather A) be an innkeeper, B) be a journalist, or C) be a party planner?")
if answer == "A":
    lorelai_points += 1
elif answer == "B":
    rory_points += 1
elif answer == "C":
    emily_points += 1


#End: determine results
if rory_points >= lorelai_points and rory_points > emily_points: 
    print("You are Rory Gilmore!")
elif lorelai_points >= rory_points and lorelai_points > emily_points: 
    print("You are Lorelai Gilmore!")
elif emily_points >= rory_points and emily_points > lorelai_points:
    print("You are Emily Gilmore!")