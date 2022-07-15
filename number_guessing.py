from multiprocessing.spawn import import_main_path
import random
import math
name=input("Hello Friend,what is your name?\n")
print("Welcome to the number guessing game "+name+".\n\tLet's begin.")


#Taking Inputs
lower=int(input("Enter lower bound for the number: "))
upper=int(input("Enter upper bound for the number: "))
#Generating random number between lower and upper bound
x=random.randint(lower,upper)
print("Guess the number between ",lower,"-",upper)
print("\n\tYou've only ",round(math.log(upper-lower+1,2))," chances to guess the integer!\n")

#Initializing number of guesses
count=0

#for calculating minimum number of guesses depends on range
while count<math.log(upper-lower+1,2):
    count+=1

    #taking input guess number
    guess=int(input("Guess a number: "))

    #condition check
    if x==guess:
        print("Congratulations ! " + name+" You did it in ",count," try.")
        #once successful guess loop will break
        break
    elif x<guess:
        print("You guessed too high!\n Guess again")
    elif x>guess:
        print("You guessed too low!\nGuess again")

    #if chance limit crosses
    if count>=math.log(upper-lower+1,2):
        print("\n The number is "+str(x))
        print("\tBetter Luck nextxt Time!") 








