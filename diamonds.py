"""
module for drawing diamond shapes with ascii art
"""

class Diamond:

    def __init__(self, size, filled=False):
        self.size = size
        self.filled = filled

    def _unfilled_diamond(self):
        """
        returns a str, unfilled diamond based on object size
        """

        for i in range(self.size):
            print(" " * (self.size - i - 1), end="")
            print("/", end="")
            print(" " * (i * 2), end="")
            print("\\")

        for i in range(self.size):
            print(" " * i, end="")
            print("\\", end="")
            print(" " * ((self.size - i - 1) * 2), end="")
            print("/")

    def _filled_diamond(self):
        """
        returns a str, filled diamond based on object's size
        """

        for i in range(self.size):
            print(" " * (self.size - i - 1), end="")
            print("/" * (i+1), end="")
            print("\\" * (i+1))

        for i in range(self.size):
            print(" " * i, end="")
            print("\\" * (self.size - i), end="")
            print("/" * (self.size - i))

    def draw_diamond(self):
        if self.filled:
            self._filled_diamond()
        else:
            self._unfilled_diamond()