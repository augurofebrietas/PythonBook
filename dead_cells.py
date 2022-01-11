"""
Based on Conway's game of life, simulation of cells
Cells with 2 or 3 neighbors stay alive, dead cells with 3 neighbors become alive, all other cells die
"""

import random, sys, time


#size of the cell grid
WIDTH = 20
HEIGHT = 79

ALIVE = "O"
DEAD = " "


def initial_sim():
    """
    create initial cell grid generating random states for each cell

    returns dict, position and state of each cell
    """

    cells = {}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.randint(0,1) == 0:
                cells[(x,y)] = DEAD
            else:
                cells[(x,y)] = ALIVE

    return cells


def display_cells(cells):
    """
    cells: dict, contains x & y coordinates and values for each cell

    prints a visual display of current cell values
    """

    for x in range(WIDTH):
        for y in range(HEIGHT):
            print(cells[(x,y)], end="")
        print()


def run_sim(cells):
    """
    cells: dict, contains x & y coordinates and values for each cell

    returns an updated dict of cells with new values based on position
    """

    updated_cells = {}

    for x in range(WIDTH):
        for y in range(HEIGHT):

            left = (x-1) % WIDTH
            right = (x+1) % WIDTH
            above = (y-1) % HEIGHT
            below = (y+1) % HEIGHT

            neighbors = [(left, above), (x, above), (right, above), (left, y), (right, y), (left, below), (x, below), (right, below)]
            count = 0

            for i in neighbors:
                if cells[i] == ALIVE:
                    count += 1

            if cells[(x,y)] == ALIVE and (count == 2 or count == 3):
                updated_cells[(x,y)] = ALIVE
            elif cells[(x,y)] == DEAD and count == 3:
                updated_cells[(x,y)] = ALIVE
            else:
                updated_cells[(x,y)] = DEAD

    return updated_cells


def main():
    """
    main loop, will continue to run sims every second until user quits program
    """

    cells = initial_sim()

    while True:
        print("\n" * 3)
        display_cells(cells)
        cells = run_sim(cells)

        try:
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    main()