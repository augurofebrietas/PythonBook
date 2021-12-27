import datetime, random


def get_birthdays(number_of_birthdays):
    """
    number_of_birthdays: int, number of random birthdays to calculate

    returns a list of datetime objects to use in comparison
    """

    birthdays = []

    for i in range(number_of_birthdays):

        start = datetime.date(2001, 1, 1)

        day = datetime.timedelta(random.randint(0, 364))
        birthday = start + day
        birthdays.append(birthday)

    return birthdays


def get_matches(birthdays):
    """
    birthdays: list, list of randomly generated datetime objects representing birthdays

    returns first matching datetime object from the list of birthdays
    """

    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a+1:]):
            if birthday_a == birthday_b:
                return birthday_a


def main():
    """
    Takes an integer input between 0 and 100 and randomly generates list of birthdays and checks for matches
    Subsequently runs 100,000 more simulations to generate an average probability of matching birthdays
    """
    
    MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

    print("This simulation generates a number of birthdays and runs them through a program to see if there are any matches.")

    while True:
        print("------")
        num = input("Enter number of birthdays to generate: ")

        try:
            num = int(num)
            if 0 < num <= 100:
                break
            else:
                print("Invalid input")

        except ValueError:
            print("Invalid input")
            continue

    birthdays = get_birthdays(num)
    print("Here are the birthdays: ")

    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(", ", end="")
        print(f"{MONTHS[birthday.month-1]} {birthday.day}", end="")
    
    print()
    print("------")

    match = get_matches(birthdays)
    if match == None:
        print("There are no matching birthdays")
    else:
        print(f"Multiple people have a birthday on {MONTHS[match.month-1]} {match.day}")

    print("Generating 100,000 more simulations...")
    input("Press Enter to continue: ")
    print("------")

    matches = 0
    for i in range(100000):
        if i % 10000 == 0:
            print(f"{i} simulations run...")
        birthdays = get_birthdays(num)
        if get_matches(birthdays) != None:
            matches += 1
    
    print("------")
    print("Finished running simulations!")
    print(f"There were matching birthdays in {matches} simulations.")
    print(f"There is a {round(matches/100000 * 100, 2)}% of having a matching birthday in a group of {num} people!")


if __name__ == "__main__":
    main()