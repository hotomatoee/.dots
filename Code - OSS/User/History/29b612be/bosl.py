from random import randint

correct_number = randint(0, 100)


def guess():
    usr_guess = int.input("what is your guess")
    if usr_guess == correct_number:
        print(f"Youre right!{usr_guess} is the right number")
    if usr_guess > correct_number:
        print(f"Your number {usr_guess} is too big")
        guess()
    if usr_guess < correct_number:
        print(f"Your number {usr_guess} is too small")
        guess()


print(correct_number)
guess()