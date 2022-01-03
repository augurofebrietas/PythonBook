"""
Allows user to encrypt and decrypt messages using the Caesar cipher
Caesar cipher shifts letters across the alphabet using a certain key
"""

import random, string, sys


UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase


def encrypt(message):
    """
    message: str, the message to encrypt

    returns the encrypted message, and the randomly generated key used to encrypt it
    """

    key = random.randint(1, 25)

    encrypted = ""

    for i in message:
        if i in UPPER:
            num = UPPER.find(i) + key
            if num >= len(UPPER):
                num -= len(UPPER)
            encrypted += UPPER[num]
        
        elif i in LOWER:
            num = LOWER.find(i) + key
            if num >= len(LOWER):
                num -= len(LOWER)
            encrypted += LOWER[num]

        else:
            encrypted += i

    print("------")
    print(f"Encrypted message: {encrypted}")
    print(f"Key used to encrypt: {key}")


def decrypt(message, key):
    """
    message: str, the message to decrypt
    key: int between 0-25, how many places to shift cipher in order to decrypt message

    prints the decrypted message
    """

    decrypted = ""

    for i in message:
        if i in UPPER:
            num = UPPER.find(i) - key
            if num < 0:
                num += len(UPPER)
            decrypted += UPPER[num]
        
        elif i in LOWER:
            num = LOWER.find(i) - key
            if num < 0:
                num += len(LOWER)
            decrypted += LOWER[num]

        else:
            decrypted += i

    print("------")
    print(f"Decrypted message: {decrypted}")


def main():
    """
    main loop, asks user to encrypt or decrypt a message
    decrypting message requires a key, encrypting will generating key randomly and give it to user afterwards
    """

    print("Caesar cipher!")

    while True:
        print("------")
        command = input("Enter 'e' to encrypt a message or 'd' to decrypt: ").lower()

        if command == "e":
            message = input("Enter the message to encrypt: ")
            encrypt(message)
        
        elif command == "d":
            message = input("Enter the message to decrypt: ")
            key = input("Enter the key (0-25): ")
        
            try:
                key = int(key)
                if 0 <= key < 26:
                    decrypt(message, key)
                else:
                    print("Invalid key")
                    
            except ValueError:
                print("Invalid key")

        more = input("Would you like to process more messages (y or n)?: ").lower()
        if more == "y":
            continue
        else:
            break

    sys.exit()


if __name__ == "__main__":
    main()