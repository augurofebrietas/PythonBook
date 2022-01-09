"""
Collatz sequence, shows way in which any positive number can be reduced down to 1
if even, n/2; if odd, n*3 + 1
"""


def collatz(num):
    """
    num, positive int used in collatz sequence

    returns list of sequential numbers before reaching 1
    """

    nums = []

    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        nums.append(str(num))

    return nums


def main():
    """
    asks for user to input an integer to generate collatz sequence
    """

    print("The collatz sequence shows the process by which any positive integer can eventually reach the number 1!")

    while True:
        num = input("Enter a positive integer: ")

        try:
            num = int(num)
        except ValueError:
            print("Not a positive integer...")
        else:
            if num > 0:
                sequence = collatz(num)
                break
            else:
                print("Not a positive integer...")

    print("-> ".join(sequence))


if __name__ == "__main__":
    main()