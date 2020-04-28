import random

# adding upper limit
limit = 5
# score tracking variables
wins = losses = 0
# main game loop
play_again = "y"
while play_again == "y":
    # generate a random number
    win_number = random.randint(1, limit)
    #input validation
    valid = False
    while not valid:
        guess = input(f"Guess the lucky number (between 1 and {limit}):")
        print() #this function is to skip a line after input
        if guess.isnumeric():
            num_guess = int(guess)
        # we can never get a value error here because we know guess is numeric
            if num_guess in range(1, limit + 1):
                valid = True

    if num_guess == win_number:
        print(f"The lucky number is {win_number}")
        wins += 1
        print("Wow! Such a genius!")
    else:
        losses += 1
        print("You suck at this!")
    print()
    print(f"Score:wins{ wins}, losses{ losses}")
    print()
    play_again = input("Do you dare to play again? (y/n)")


