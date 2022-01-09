"""
Clickbait headline generator
Randomly generates different clickbait-style headlines based on templates
"""

import random


OBJECT_PRONOUNS = ["her", "him", "them"]
POSSESIVE_PRONOUNS = ["her", "his", "their"]
PERSONAL_PRONOUNS = ["she", "he", "they"]
STATES = ["California", "Texas", "Florida", "New York", "Pennsylvania"]
NOUNS = ["athlete", "clown", "shovel", "paleo diet", "video game", "avocado", "plastic straw",
"serial killer", "dog", "cat"]
PLACES = ["house", "attic", "bank deposit box", "school", "basement", "workplace", "donut shop"]
WHEN = ["soon", "this year", "later today", "next week"]

headline_options = ["m", "w", "c", "y", "d", "g", "r", "j"]


def millenial_headline():
    return f"Are millenials killing the {random.choice(NOUNS)} industry??"


def what_headline():
    return f"Without this {random.choice(NOUNS)}, {random.choice(NOUNS)}s could kill you {random.choice(WHEN)}."


def company_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)

    return f"Big companies hate {pronoun}! See how this {state} {noun1} invented a cheaper {noun2}!"


def you_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)

    return f"You won't believe what this {state} {noun} found in {pronoun} {place}!"


def dont_headline():
    return f"What {random.choice(NOUNS)}s don't want you to know about {random.choice(NOUNS)}s"


def gift_headline():
    return f"{random.randint(7,15)} gift ideas to give your {random.choice(NOUNS)}"


def reasons_headline():
    number1 = random.randint(3,19)
    noun = random.choice(NOUNS)
    number2 = random.randint(1, number1)

    return f"{number1} reasons why {noun}s are more interesting than you think. (Number {number2} will surprise you!)"


def generate_headline(type=None):
    """
    type: str, optional argument representing type of headline to generate
    if no argument is passed, choose one at random

    prints str, filled in clickbait headline
    """

    if type == None:
        type = random.choice(headline_options)

    if type == "m":
        print(millenial_headline())
    elif type == "w":
        print(what_headline())
    elif type == "c":
        print(company_headline())
    elif type == "y":
        print(you_headline())
    elif type == "d":
        print(dont_headline())
    elif type == "g":
        print(gift_headline())
    elif type == "r":
        print(reasons_headline())


def main():
    """
    main program, asks for user input about which type of headline to generate
    or just generate a random one
    """

    print("Clickbait headline generator!")
    print("We can generate some different types of headlines:")
    print("-(M)illenials are killing...\n-(W)hat you don't know...\n-(C)ompanies hate them!...\n-(Y)ou won't believe!")
    print("-(D)on't want you to know...\n-(G)ift idea...\n-(R)easons why...")
    print("------")

    while True:
        command = input("Enter one of the above commands, or just press Enter for a completely random headline: ").lower()

        if command == "":
            generate_headline()
            break
        elif command in headline_options:
            generate_headline(command)
            break
        else:
            print("Invalid command")

    print("poop")


if __name__ == "__main__":
    main()


