import argparse
from enum import Enum
from argparse import ArgumentParser

def convert(number: str):
    result = 0

    switcher = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Parsing number
    i = 0
    while i < len(number):
        # Subtract previous number
        if (i > 0 and len(number) >= 2) and switcher.get(number[i]) > switcher.get(number[i - 1]):
            result -= switcher.get(number[i - 1])
            result += switcher.get(number[i]) - switcher.get(number[i - 1])
        else:
            result += switcher.get(number[i])

        i += 1

    return result


def init_argparse():
    parser = argparse.ArgumentParser("roman-converter")
    parser.add_argument("NUMBER", help="roman number as string")
    return parser


def start():
    parser = init_argparse()
    args = parser.parse_args()

    if args.NUMBER is not None:
        print(convert(args.NUMBER))


if __name__ == "__main__":
    start()
