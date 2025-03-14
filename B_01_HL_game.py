import math


def yes_no(question):
    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter a yes / no")


def instructions():
    print('''
To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the
secret number will be between 1 and 100).

Then choose how many rounds you'd like to player <enter> 
for infinite mode.

Your goal is to try to guess the secret number without 
running out of guesses.

    Good luck.


    ''')


def int_check(question, low=None, high=None, exit_code=None):

    if low is None and high is None:
        error = "please enter integer"

    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    else:
        error = (f"plase enter an integer"
                 f" is between {low} and {high} inclusive")
    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


mode = "regular"
rounds_played = 0


print("Welcome to the higher lower game")
print()

want_instructions = yes_no("Do you want to see the instructions? ")
print(f"you chose {want_instructions}")

# Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()


num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

low_num = int_check("Low Number? ")
high_num = int_check("High Number? ", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)

while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode) "

    else:
        rounds_heading = f"\n round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    if mode == "infinite":
        num_rounds += 1



