import random

# adding upper limit
limit = 10
# score tracking variables
# wins = losses = 0
score: int = 0

# This is creating our own function to test input validation so that we don't have to be repetitive.
def get_valid_number():
    valid = False
    while not valid:
        guess = input(f"Guess the lucky number (between 1 and {limit}):")
        if guess.isnumeric() and int(guess) in range(1, limit + 1):
            valid = True
            return int(guess)

# main game loop
play_again = "y"
while play_again == "y":
    # User's first chance:
    win_number = random.randint(1, limit)
    num_guess = get_valid_number()
    if num_guess == win_number:
        print(f"The lucky number is {win_number}")
        print()
        print("Awesome! You nailed it on the first try!")
        score += 5
    elif num_guess > win_number:
        print()
        print("Aww, poor looser! Try guessing lower this time.")
        print()
    else:
        print()
        print("What are you stupid? Guess higher this time.")
        print()
    # User's second chance:
    if num_guess != win_number:
        num_guess = get_valid_number()
        if num_guess == win_number:
            score += 3
            print()
            print("Hooray! You guessed correctly! I'm proud of you!")
            print()
        elif num_guess > win_number:
            print()
            print("You're not that smart are you? Why don't you guess lower this time?")
            print()
        else:
            print("I really thought you would get it right this round! Guess higher.")
            print()
    # User's final chance:
    if num_guess != win_number:
        num_guess = get_valid_number()
        if num_guess == win_number:
            print()
            score += 1
            print("Finally! You guessed the correct number!")
            print()
        else:
            print(f"You're a failure that can't guess a simple number! The winning number is {win_number}")
            print()

    print(f"Score:{score}")
    print()

    play_again = input("Do you dare to play again? (y/n)")
    print()
