# Functions go here
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


print()
print(" Welcome to the higher, lower game")
print()


# Main routine
want_instructions = yes_no("Do you want to see the instructions? ")
print(f"you chose {want_instructions}")

# Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()

print()
print("Program continues")