"""
A simple forest fire simulation to demonstrate emergent behavior

For each step of the sim, there is a 1% chance for a new tree to grow, and a 1% chance of lightning strike
If a tree catches fire, adjacent trees will also catch fire
"""

import random, sys, time
import bext


WIDTH = 50
HEIGHT = 22

TREE = "A"
FIRE = "W"
INITIAL_DENSITY = 0.20
GROWTH_CHANCE = 0.01
FIRE_CHANCE = 0.01

PAUSE_LENGTH = 0.5


def create_new_forest():
    """
    returns dict, representing new forest data structure
    """

    forest = {"width" : WIDTH, "height" : HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_DENSITY:
                forest[(x,y)] = TREE
            else:
                forest[(x,y)] = " "

    return forest


def display_forest(forest):
    """
    forest: dict, (x,y) coords with associated values (either tree or empty space)

    prints a visual representation of the data
    """

    bext.goto(0,0)
    for y in range(forest["height"]):
        for x in range(forest["width"]):
            if forest[(x,y)] == TREE:
                bext.fg("green")
                print(TREE, end="")
            elif forest[(x,y)] == FIRE:
                bext.fg("red")
                print(FIRE, end="")
            elif forest[(x,y)] == " ":
                print(" ", end="")
        print()


def main():
    """
    displays current step of simulation
    then creates next step of sim based on information in current step
    1% chance of tree growing and 1% chance of lightning striking
    fire spreads to adjacent trees
    """

    forest = create_new_forest()
    bext.clear()

    while True:
        display_forest(forest)

        next_forest = {
            "width" : forest["width"],
            "height" : forest["height"]
        }

        for x in range(forest["width"]):
            for y in range(forest["height"]):
                if (x,y) in next_forest:
                    continue

                if forest[(x,y)] == " " and random.random() <= GROWTH_CHANCE:
                    next_forest[(x,y)] = TREE
                elif forest[(x,y)] == TREE and random.random() <= FIRE_CHANCE:
                    next_forest[(x,y)] = FIRE
                elif forest[(x,y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x + ix),(y + iy)) == TREE:
                                next_forest[(x + ix),(y + iy)] = FIRE
                    next_forest[(x,y)] = " "
                else:
                    next_forest[(x,y)] = forest[(x,y)]

        forest = next_forest
        time.sleep(PAUSE_LENGTH)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()