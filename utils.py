#!/usr/bin/env python3

import random
import string


chars = string.ascii_letters + string.digits + "+-*%$#@!()^"


def generate_passwords(number: int, length: int) -> None:
    for ln in range(number):
        password = ""
        for char in range(length):
            password += random.choice(chars)
        print(password)


def main():
    number = int(input("Enter number of passwords to generate:\t"))
    length = int(input("Enter length of each password:\t"))
    generate_passwords(number, length)


if __name__ == "__main__":
    main()
