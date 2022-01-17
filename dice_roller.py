"""
Virtual dice roller for simulating dice rolls in D&D and similar games
"""

import random


class Dice:

    def __init__(self, sides):
        self.sides = sides
        self.number = random.randint(1,sides)

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return self.number + other.number

    def roll_dice(self):
        self.number = random.randint(1, self.sides)


def display_dice(dice):
    """
    dice: list of dice objects

    prints a display of dice and their sums
    """

    total = 0
    dice_str = ""

    for i in dice:
        total += i.number
        dice_str += f"|{i.number}| "

    print(f"Dice: {dice_str}")
    print(f"Total: {total}")


def main():
    """
    main program, asks user for input: how many dice to roll and how many sides
    """

    print("Dice roller")
    dice = []

    while True:
        print("------")
        
        amount = input("How many dice to roll?: ")
        size = input("What size dice? (Number of sides): ")

        try:
            amount = int(amount)
            size = int(size)
        except ValueError:
            print("Please enter an integer representing size of dice and number to roll")
            continue
        else:
            for i in range(amount):
                dice.append(Dice(size))
            break

    while True:
        print("------")
        display_dice(dice)
        command = input("Roll again? (y or n): ").lower()

        if command == "y":
            for i in dice:
                i.roll_dice()
        else:
            break


if __name__ == "__main__":
    main()


    