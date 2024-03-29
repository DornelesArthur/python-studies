import random as r

print("****************************")
print("Welcome to guess the number!")
print("****************************")

secret_number = r.randrange(1,101)
number_chances_difficulties = [8,6,4]
choose_diff = True
try:
    while choose_diff:
        print("(0) Easy\n(1) Medium\n(2) Hard")
        difficulty = int(input("Choose a difficulty:"))
        try:
            number_chances = number_chances_difficulties[difficulty]
            choose_diff = False
        except IndexError:
            print("Invalid value!")

    while (number_chances):
        guess = int(input(f"Guess the number ({number_chances} chances left): "))

        print("Your guess is: ", guess)

        correct = secret_number == guess
        higher = secret_number > guess
        if(correct):
            print("You have guess correctly")
            number_chances = 0
        else:
            if (higher):
                print("The secret number is higher than ", guess)
            else:
                print("The secret number is lower than ", guess)
            number_chances-=1
    print("Game has ended")
    if(not correct):
        print(f"The right number was: {secret_number}")
except ValueError:
    print("Only numbers are accepted!")
