#!/usr/bin/env python3

__author__ = "Shalapai4ek"
__version__ = "1.0.0"

import argparse
import secrets
import string
import sys

def generate_password(length=12):
    all_char = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(all_char) for _ in range(length))

    return password

def main():
    parser = argparse.ArgumentParser(description="Simple password generator on python")

    parser.add_argument(
            '-l', '--length',
            type=int,
            default=12,
            help="Password lenght (by default: 12)"
            )

    args = parser.parse_args()

    result = generate_password(length=args.length)
    print(result)

if __name__ == "__main__":
    main()

