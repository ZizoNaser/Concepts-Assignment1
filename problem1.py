#! /usr/bin/env python3

"""Answer to problem #1 in assignment 1 [concepts].

Problem:
--------

Given: A positive integer and an array ​ A ​ [1..​ n ​ ] ​ of integers
        and a positive number ​ k ​ ≤ ​ n.
Return: The ​ k ​ -th smallest element of ​ A.

Authors:
--------

Abdel-aziz Abdel-naser    20140168  CS_IS_2
Abdullah Abdel-meneim     20140171  CS_IS_2

"""


def get_kth_smallest(length, array, k):
    """Return the K(th) smallest value in a list."""
    # Copy the list content to avoid changing the oraginal list.
    new_array = array.copy()
    # # Remove duplicates.
    # new_array = list(set(new_array))
    # Sort the list.
    new_array.sort()
    # Select and return the kth smallest value.
    return new_array[k-1]


if __name__ == '__main__':
    print("Please enter the list's length:")
    length = int(input())
    print("Please enter the data, on one line:")
    array = []
    tmp = input().split()
    for i in range(0, length):
        array.append(int(tmp[i]))
    print("Now enter the position (k):")
    k = int(input())
    value = get_kth_smallest(length, array, k)
    print(value)

    # length = 11
    # array = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]
    # k = 8
    # print(get_kth_smallest(length, array, k))
