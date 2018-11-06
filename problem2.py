#! /usr/bin/env python3

"""Answer to problem #2 in assignment 1 [concepts].

Problem:
--------

Write a program that get factors of a number and display it.

Authors:
--------

Abdel-aziz Abdel-naser    20140168  CS_IS_2
Abdullah Abdel-meneim     20140171  CS_IS_2

"""


def get_factors_of(num):
    """Return a list of number's factors."""
    # Prepare a return list.
    factors = []
    # Loop on all the number in [0,num) check which is a factor.
    for x in range(1, num+1):
        if num % x == 0:
            # If a factor add to the return list.
            factors.append(x)
    return factors


if __name__ == "__main__":
    print("please enter the number:")
    number = int(input())
    print("The factors of %d are:" % number)
    for num in get_factors_of(number):
        print(num)
