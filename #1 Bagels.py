"""
Number guessing game
Player is given 10 tries to guess a 3-digit number and receives clues after each guess
Pico: correct digit, wrong place
Fermi: correct digit, right place
Bagels: no correct digits
"""


import random

MAX_GUESSES = 10


def generate_number():
    """
    generates random 3 unique digit number, returned as a string
    """
    nums = list("0123456789")
    random.shuffle(nums)
    
    return "".join(nums[0:3])


def get_clues(guess, secret_num):
    """
    guess: str, the number guessed by player
    secret_num: str, the randomly generated numebr the player is trying to guess

    prints clues for each digit
    """

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("fermi")
        elif guess[i] in secret_num:
            clues.append("pico")

    random.shuffle(clues)
    if clues == []:
        print("bagels")
    else:
        print(", ".join(clues))


def main():
    """
    runs the main game loop, player has 10 guesses to get the secret number
    receives clues based on their guess if they do not guess correctly
    """
    
    secret_number = generate_number()
    guesses = 0
    win = False

    print("Welcome to Bagels, a number guessing game!")
    print("~Clues~")
    print("Pico: digit is correct but in wrong position\nFermi: digit is correct and in right position\nBagels: no correct digits")

    while guesses < MAX_GUESSES:

        print("------")
        print(f"{abs(guesses-10)} guesses left...")
        guess = input("Enter a 3-digit number: ")

        if guess == secret_number:
            win = True
            break

        else:
            if len(guess) != 3 or not guess.isdigit():
                print("Invalid input")
                continue
            
            else:
                get_clues(guess, secret_number)

        guesses += 1

    print("------")
    if win:
        print("You got it!")
    else:
        print("You ran out of tries...")
        print(f"The number was {secret_number}")


if __name__ == "__main__":
    main()