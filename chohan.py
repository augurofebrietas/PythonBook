"""
Traditional Japanese gambling game, dealer rolls 2 dice and player must
pick between cho(even) or han(odd)
"""

import random, sys


JAPANESE_NUMBERS = {
    1: "ichi",
    2: "ni",
    3: "san",
    4: "shi",
    5: "go",
    6: "roku"
}


class Dice:

    def __init__(self):
        self.value = random.randint(1,6)
        self.name = JAPANESE_NUMBERS[self.value]

    def __add__(self, other):
        return self.value + other.value

    def roll_again(self):
        self.value = random.randint(1,6)
        self.name = JAPANESE_NUMBERS[self.value]


def get_bet(total_money):
    """
    total_money: int, representing the total amount of money player can bet

    returns int, valid number for bet
    """

    while True:
        print("------")
        print(f"You have {total_money} mon.")
        bet = input(f"How much would you like to bet? (1-{total_money}): ")

        try:
            bet = int(bet)
        except ValueError:
            print("Invalid bet")
        else:
            if 1 <= bet <= total_money:
                break
            else:
                print("Invalid bet")

    return bet


def check_guess():
    """
    checks if user inputs a valid option (either cho or han)

    returns guess if valid
    """

    while True:
        print("------")
        guess = input("Is it cho(even) or han(odd)?: ").lower()

        if guess == "cho" or guess == "han":
            return guess
        else:
            print("Not a valid guess...")


def main():
    """
    main game loop, computer rolls 2 dice, and player must guess whether
    the total is cho(even) or han(odd)
    """

    print("Welcome to Cho-han!")
    print("The dealer will roll 2 dice, you must guess whether the total is cho(even) or han(odd).")

    money = 5000

    while money > 0:
        bet = get_bet(money)

        dice1 = Dice()
        dice2 = Dice()

        print("The dealer rolls the dice...")
        guess = check_guess()

        if (dice1 + dice2) % 2 == 0:
            result = "cho"
        else:
            result = "han"

        print(f"Dealer reveals:\n|{dice1.value} - {dice1.name}| |{dice2.value} - {dice2.name}|")
        print(f"It's {result}!")

        if guess == result:
            print(f"You win {bet} mon!")
            money += bet
        else:
            print(f"You lose {bet} mon!")
            money -= bet

        print("------")
        command = input("Keep playing? Press enter to continue or type 'quit' to stop: ").lower()

        if command == "quit":
            sys.exit()

    print("Sorry, you are out of money!")

    
if __name__ == "__main__":
    main()

