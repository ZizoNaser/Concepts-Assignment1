#! /usr/bin/env python3

"""Answer to problem #3 in assignment 1 [concepts].

Problem:
--------

A positive integer is called an Armstrong number of order n
if abcd... = an + bn + cn + dn + ...
For example,
153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 is an Armstrong number.
Your program will take start and end interval as input then print all Armstrong
number in this interval.

Authors:
--------

Abdel-aziz Abdel-naser    20140168  CS_IS_2
Abdullah Abdel-meneim     20140171  CS_IS_2

"""


def get_armstrong(lower, upper):
    """Return all Armstrong numbers between two values."""
    armstrongs = []

    def is_armstrong(num):
        """Check if a number is an Armstrong number."""
        length = len(str(num))
        sum = 0
        num_copy = num
        while num_copy > 0:
            digit = num_copy % 10
            sum += digit ** length
            num_copy //= 10
        if num == sum:
            return True
        else:
            return False

    for x in range(lower, upper+1):
        if is_armstrong(x):
            armstrongs.append(x)
    return armstrongs


if __name__ == '__main__':
    print("Please Enter the starting and ending values. in one line:")
    tmp = input().split()
    tmp.sort()
    for number in get_armstrong(int(tmp[0]), int(tmp[1])):
        print(number)
