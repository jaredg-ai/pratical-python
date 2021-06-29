#in order to use a module, you first need to import it.
import random
#now you can use it. this function will return a random number between 1 and 6.
roll = random.randint(1,6)
#this wil print the result. The str(roll) will convert the int into a string.
print("The computer rolled a " + str(roll))
#here, we want to convert the input to an int so we can compare to roll.
guess = int(input("guess the dice roll:\n"))

if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print("Wrong! They rolled a " + str(roll))