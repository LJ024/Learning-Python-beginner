import random

#score tracking variables
wins = losses = 0
play_again = "y"
while play_again == "y":
    # generate a random number
    win_number = random.randint(1, 3)
    guess = int(input("Chose a number between 1 and 3 to play:"))
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

