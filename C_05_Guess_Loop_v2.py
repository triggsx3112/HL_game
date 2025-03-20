


def int_check(question, low=None, high=None, exit_code=None):

    if low is None and high is None:
        error = "please enter integer"

    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    else:
        error = (f"please enter an integer"
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




secret = 7


low_num = 0
high_num = 10
guesses_allowed = 5


guesses_used = 0
already_guessed = []


guess = ""
while guess != secret and guesses_used < guesses_allowed:

    guess = int_check("guess: ", low_num, high_num)

    if guess == "xxx":
        end_game = "yes"
        break


    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've used "
              f"{guesses_used} / {guesses_allowed} guessed")
        continue

    else:
        already_guessed.append(guess)

    guesses_used += 1


    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Too low, please try a higher number "
                    f"You've used {guesses_used} / {guesses_allowed}")


    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high, please try a lower number "
                    f"You've used {guesses_used} / {guesses_allowed}")


    elif guess == secret:

        if guesses_used == 1:
            feedback = "Lucky, you got it on the first guess"
        elif guesses_used == guesses_allowed:
            feedback = f"phew, you got it in {guesses_used}."
        else:
            feedback = f"Well done, you guessed the secret number in {guesses_used} guesses"

    else:
        feedback = "Sorry -  you have no more guesses. You lose this round"

    print(feedback)

    if guesses_used == guesses_allowed - 1:
        print("\nCareful - you have one guess left \n")

print()
print("end of round")