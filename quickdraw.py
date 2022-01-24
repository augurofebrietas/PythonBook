"""
Super simple program to test your reflexes
"""

import random, sys, time


def check_draw_time(time):
    """
    time: float, amount of time the player took to press Enter
    prints rounded time and checks whether player won or lost
    """

    if time < 0.01:
        print("You pressed too soon! You lose!")
    
    elif time > 0.3:
        print(f"You took {round(time, 4)} seconds to draw. You lose!")
    
    else:
        print(f"You took {round(time, 4)} seconds to draw...")
        print("You win!")


def main():
    """
    main program loop
    delays draw command using time module, checks players response time using input()
    """

    while True:
        print("------")
        print("Test your reflexes!")
        print("When you see DRAW, you have 0.3 seconds to press Enter...")
        print("Don't press too late or before the word appears or you lose")
        print()
        input("Press Enter to begin...")

        print("Get ready...")
        time.sleep(random.randint(20, 50) / 10)
        print("DRAW!")

        draw_time = time.time()
        input()

        time_elapsed = time.time() - draw_time
        check_draw_time(time_elapsed)

        command = input("Play again? Press Enter to continue or 'Q' to quit: ").lower()

        if command == "q":
            print("Thanks for playing!")
            sys.exit()


if __name__ == "__main__":
    main()