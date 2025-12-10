from random import randint

correct_number = randint(0, 100)
tries = 0

def guess():
    usr_guess = int(input("what is your guess"))
    if usr_guess == correct_number:
        print(f"Youre right!{usr_guess} is the right number")
        print(f"It took you {tries} tries")
    if usr_guess > correct_number:
        print(f"Your number {usr_guess} is too big")
        tries = tries + 1
        guess()
    if usr_guess < correct_number:
        print(f"Your number {usr_guess} is too small")
        tries = tries + 1
        guess()


print(correct_number)
guess()