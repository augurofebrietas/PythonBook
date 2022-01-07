"""
Calendar generator program
Takes user input for month and year and uses datetime module
to create a janky text calendar
"""


import datetime


DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August",
"September", "October", "November", "December")


def generate_calendar(year, month):
    """
    year: int, numeric year greater than zero
    month: int, between 1 and 12, representing a month to generate

    returns string, a text version of the calendar based on year and month values
    """

    calendar_text = ""

    #put month at year at top of calendar
    calendar_text += (" " * 34) + MONTHS[month-1] + " " + str(year) + "\n"

    #add days labels
    calendar_text += "...Sunday...Monday...Tuesday...Wednesday...Thursday...Friday...Saturday..\n"

    week_separator = ("+----------" * 7) + "\n"
    blank_row = ("|          " * 7) + "\n"

    current_date = datetime.date(year, month, 1)

    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    #generate main calendar text
    while True:
        calendar_text += week_separator

        #first row with day number labels
        day_number_row = ""

        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += "|" + day_number_label + (" " * 8)
            current_date += datetime.timedelta(days=1)
        day_number_row += "|\n"

        calendar_text += day_number_row
        for i in range(3):
            calendar_text += blank_row

        if current_date.month != month:
            break

    calendar_text += week_separator
    
    return calendar_text


def main():
    """
    main program, takes user input for year and month and outputs text calendar
    also saves to a new text file
    """

    print("Generate a calendar!")

    while True:
        year = input("Enter a year for the calendar: ")

        try:
            year = int(year)
            if year > 0:
                break
            else:
                print("Year must be greater than 0")
        except ValueError:
            print("Please enter a numeric year, like 2022")
        finally:
            print("------")
            
    while True:
        month = input("Okay, now enter the number of the month you want to generate (1-12): ")

        try:
            month = int(month)
            if 1 <= month <= 12:
                break
            else:
                print("Enter a number between 1 and 12")
        except ValueError:
            print("Please enter a numeric month, like 3 for March")
        finally:
            print("------")

    calendar = generate_calendar(year, month)
    print(calendar)

    filename = f"{month}_{year}_calendar"

    with open(filename, "w") as file:
        file.write(calendar)

    print(f"Saved to {filename}")


if __name__ == "__main__":
    main()
