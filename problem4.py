#! /usr/bin/env python3

"""Answer to problem #4 in assignment 1 [concepts].

Problem:
--------

Convert number from base a to base b
Your program will take number in base a then convert it to base b

Authors:
--------

Abdel-aziz Abdel-naser    20140168  CS_IS_2
Abdullah Abdel-meneim     20140171  CS_IS_2

"""


def convert_to_base(num, base_a, base_b):
    "Convert a number from base a to base b."
    num = int(str(num), base_a)
    if base_b == 2:
        result = bin(num).replace('0b', '')
    elif base_b == 8:
        result = oct(num).replace('0o', '')
    elif base_b == 10:
        result = str(num)
    elif base_b == 16:
        result = hex(num).replace('0x', '')
    else:
        raise "Unkown base"
    return result


if __name__ == '__main__':
    print("Enter number:")
    number = int(input())
    print("Enter the number base")
    base_a = int(input())
    print("Convert it to base?")
    base_b = int(input())
    print(convert_to_base(number, base_a, base_b))
