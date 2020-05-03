import random

# adding upper limit
limit =10
# score tracking variables
#wins = losses = 0
score = 0
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
        score += 5
        print()
        print("Awesome! You nailed it on the first try!")
    elif num_guess > win_number:
        print ()
        print("Aww, poor looser! Try guessing lower this time.")
        print()
    else:
        print ()
        print("What are you stupid? Guess higher this time.")
        print()

    if num_guess != win_number:
        valid = False
        while not valid:
            guess = input (f"Guess the lucky number (between 1 and {limit}):")
            print()
            if guess.isnumeric ():
                num_guess = int(guess)
                # we can never get a value error here because we know guess is numeric
                if num_guess in range (1, limit +1):
                    valid = True
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

    if num_guess != win_number:
        valid = False
        while not valid:
            guess = input (f"Guess the lucky number (between 1 and {limit}):")
            print()
            if guess.isnumeric ():
                num_guess = int(guess)
                # we can never get a value error here because we know is numeric
                if num_guess in range (1, limit +1):
                    valid = True
        if num_guess == win_number:
            print()
            score += 1
            print("Finally! You guessed the correct number!")
            print()
        else:
            print (f"You're a failure that can't guess a simple number! The winning number is {win_number}")
            print()

    print(f"Score:{ score}")
    print()

    play_again = input("Do you dare to play again? (y/n)")
    print()



