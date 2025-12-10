from random import randint

correct_number = randint(0, 100)
tries = 0

def guess():
    usr_guess = int(input("what is your guess"))
    if usr_guess == correct_number:
        return print(f"Youre right!{usr_guess} is the right number")
    if usr_guess > correct_number:
        print(f"Your number {usr_guess} is too big")
    if usr_guess < correct_number:
        print(f"Your number {usr_guess} is too small")
    tries =+ 1


print(correct_number)
guess()
print(tries)