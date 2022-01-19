"""
Duckling generator
"""

import random, shutil, sys, time


PAUSE = 0.2
DENSITY = .10

WIDTH = shutil.get_terminal_size()[0] - 1
DUCKLING_WIDTH = 5


class Duckling:
    """
    little string representation of a duckling with randomized features
    """

    def __init__(self):
        self.direction = random.choice(["left", "right"])
        self.body = random.choice(["chubby", "very_chubby"])
        self.mouth = random.choice(["open", "closed"])
        self.wing = random.choice(["out", "up", "down"])

        if self.body == "chubby":
            self.eyes = "beady"
        else:
            self.eyes = random.choice(["beady", "wide", "happy", "aloof"])

        self.display_next = "head"

    def get_head(self):
        head_string = ""

        if self.direction  == "left":
            if self.mouth == "open":
                head_string += ">"
            elif self.mouth == "closed":
                head_string += "="

            if self.eyes == "beady" and self.body == "chubby":
                head_string += '"'
            elif self.eyes == "beady" and self.body == "very_chubby":
                head_string += '" '
            elif self.eyes == "wide":
                head_string += "''"
            elif self.eyes == "happy":
                head_string += "^^"
            elif self.eyes == "aloof":
                head_string += "``"

            head_string += ") "

        elif self.direction == "right":
            head_string += " ("

            if self.eyes == "beady" and self.body == "chubby":
                head_string += '"'
            elif self.eyes == "beady" and self.body == "very_chubby":
                head_string += ' "'
            elif self.eyes == "wide":
                head_string += "''"
            elif self.eyes == "happy":
                head_string += "^^"
            elif self.eyes == "aloof":
                head_string += "``"

            if self.mouth == "open":
                head_string += "<"
            elif self.mouth == "closed":
                head_string += "="
        
        if self.body == "chubby":
            head_string += " "

        return head_string

    def get_body(self):
        body_string = "("

        if self.direction == "left":
            if self.body == "chubby":
                body_string += " "
            elif self.body == "very_chubby":
                body_string += "  "

            if self.wing == "out":
                body_string += ">"
            elif self.wing == "up":
                body_string += "^"
            elif self.wing == "down":
                body_string += "v"

        elif self.direction == "right":
            if self.wing == "out":
                body_string += "<"
            elif self.wing == "up":
                body_string += "^"
            elif self.wing == "down":
                body_string += "v"

            if self.body == "chubby":
                body_string += " "
            elif self.body == "very_chubby":
                body_string += "  "

            body_string += ")"
            if self.body == "chubby":
                body_string += " "

        return body_string

    def get_feet(self):
        if self.body == "chubby":
            return " ^^  "
        elif self.body == "very_chubby":
            return " ^ ^ "

    def get_next_part(self):
        if self.display_next == "head":
            self.display_next = "body"
            return self.get_head()
        elif self.display_next == "body":
            self.display_next = "feet"
            return self.get_body()
        elif self.display_next == "feet":
            self.display_next = None
            return self.get_feet()


def main():
    """
    creates a randomized amount of ducklings based on current terminal size
    """

    print("Duckling screensaver")
    print("Press Ctrl+C to quit...")
    time.sleep(2)

    lanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:
        for lane_num, duck in enumerate(lanes):
            if duck == None and random.random() <= DENSITY:
                duck = Duckling()
                lanes[lane_num] = duck

            if duck != None:
                print(duck.get_next_part(), end="")

                if duck.get_next_part() == None:
                    lanes[lane_num] = None

            else:
                print(" " * DUCKLING_WIDTH, end="")

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()