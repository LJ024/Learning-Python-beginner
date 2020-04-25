import random

valid = False
while not valid:
    guess = input(f"Guess the lucky number (between 1 and {limit}):")
#adding upper limit
limit = 5
#score tracking variables
wins = losses = 0
play_again = "y"
while play_again == "y":
    # generate a random number
    win_number = random.randint(1, limit)
    guess = int(input(f"Guess the lucky number (between 1 and {limit}):"))
    print()
    print(f"The lucky number is {win_number}")
    if int(guess) == win_number:
        wins += 1
        print("Wow! Such a genius!")
    else:
        losses += 1
        print("You suck at this!")
        print()
    print(f"Score:wins{wins}, losses{losses}")
    print()
    play_again = input("Do you dare to play again? (y/n)")
    print()

