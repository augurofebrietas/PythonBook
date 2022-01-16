"""
Just a simple visualization representing someone tunneling into a deep cave
"""

import random, sys, time


WIDTH = 70
PAUSE_AMOUNT = 0.05

left_width = 20
gap = 20


print("DEEP CAVE")
print("Press Ctrl+C to stop...")

time.sleep(2)

while True:
    right_width = WIDTH - gap - left_width
    print(("#" * left_width) + (" " * gap) + ("#" * right_width))

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    adjust = random.randint(1,6)
    if adjust == 1 and left_width > 1:
        left_width -= 1
    elif adjust == 2 and left_width + gap < WIDTH - 1:
        left_width += 1

    adjust_gap = random.randint(1,6)
    if adjust == 1 and gap > 1:
        gap -= 1
    elif adjust == 2 and left_width + gap < WIDTH - 1:
        gap += 1
