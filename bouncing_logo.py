"""
bouncing DVD logo animation using bext

*Do not resize terminal window while running*
"""

import sys, random, time
import bext


WIDTH, HEIGHT = bext.size()
WIDTH -= 1

LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
DIRECTIONS = ["ur", "ul", "dr", "dl"]


class Logo():

    def __init__(self):
        self.color = random.choice(COLORS)
        self.x = random.randint(1, WIDTH-4)
        self.y = random.randint(1, HEIGHT-4)
        self.dir = random.choice(DIRECTIONS)

    def change_color(self):
        new_color = self.color

        while new_color == self.color:
            new_color = random.choice(COLORS)
        
        self.color = new_color

    def change_dir(self, new_dir):
        self.dir = new_dir


def check_corners(logo):
    """
    logo: Logo object with color, x and y coords, and direction

    returns True if logo is colliding with corner, as well as corner location
    """

    if logo.x == 0 and logo.y == 0:
        return True, "dr"
    elif logo.x == 0 and logo.y == HEIGHT-1:
        return True, "ur"
    elif logo.x == WIDTH-3 and logo.y == 0:
        return True, "dl"
    elif logo.x == WIDTH-3 and logo.y == HEIGHT-1:
        return True, "ul"
    else:
        return False, None


def check_bounce(logo):
    """
    logo: Logo object with color, x and y coords, and direction

    checks if logo is colliding with an edge of the screen and change dir accordingly
    """

    #left edge
    if logo.x == 0 and logo.dir == "ul":
        logo.change_dir("ur")
    elif logo.x == 0 and logo.dir == "dl":
        logo.change_dir("dr")

    #right edge
    elif logo.x == WIDTH-3 and logo.dir == "ur":
        logo.change_dir("ul")
    elif logo.x == WIDTH-3 and logo.dir == "dr":
        logo.change_dir("dl")

    #top edge
    elif logo.y == 0 and logo.dir == "ul":
        logo.change_dir("dl")
    elif logo.y == 0 and logo.dir == "ur":
        logo.change_dir("dr")

    #bottom edge
    elif logo.y == HEIGHT-1 and logo.dir == "dl":
        logo.change_dir("ul")
    elif logo.y == HEIGHT-1 and logo.dir == "dr":
        logo.change_dir("ur")


def main():
    """
    main loop
    """

    bext.clear()
    logos = [Logo() for _ in range(LOGOS)]
    corner_count = 0

    while True:
        for logo in logos:
            bext.goto(logo.x, logo.y)
            print("   ", end="")

            original_dir = logo.dir

            is_corner, corner = check_corners(logo)
            if is_corner:
                corner_count += 1
                logo.change_dir(corner)
            else:
                check_bounce(logo)

            if logo.dir != original_dir:
                logo.change_color()

            if logo.dir == "ur":
                logo.x += 2
                logo.y -= 1
            elif logo.dir == "ul":
                logo.x -= 2
                logo.y -= 1
            elif logo.dir == "dr":
                logo.x += 2
                logo.y += 1
            elif logo.dir == "dl":
                logo.x -= 2
                logo.y += 1

        bext.goto(5,0)
        bext.fg("white")
        print(f"Corner bounces: {corner_count}")

        for logo in logos:
            bext.goto(logo.x, logo.y)
            bext.fg(logo.color)
            print("DVD", end="")

        bext.goto(0,0)

        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


if __name__ == "__main__":
    main()