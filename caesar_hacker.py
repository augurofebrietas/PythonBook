"""
Uses brute-force hacking to run through every possible decrypted version of a
message encrypted with the Caesar cipher
"""

import string


UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase


def decrypt(message, key):
    """
    message: str, message to decrypt
    key: int between 0 and 25

    returns message decrypted using the key
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

    return decrypted
    

def main():

    print("Caesar hacker!")
    message = input("Enter message to decrypt: ")

    print("------")
    print("Possible decryptions:")

    for i in range(26):
        decrypted = decrypt(message, i)
        print(f"Key({i}): {decrypted}")


if __name__ == "__main__":
    main()