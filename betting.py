import random

# generate a random number
win_number = random.randint (1, 3)
guess = input("Guess the winning number:")
print(f"The lucky number is {win_number}")
if int(guess) == win_number:
    print("Wow! Such a genius!")
else:
    print("You suck at this!")
