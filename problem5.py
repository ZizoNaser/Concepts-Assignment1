#! /usr/bin/env python3

"""Answer to problem #5 in assignment 1 [concepts].

Problem:
--------

Binary Coded Decimal (BCD) is a form of decimal representation represent 
the 10 decimal digits in terms of binary numbers each number in four bits.
Through Addition calculation for any invalid entry (any BCD digit greater 
than 1001) exists, 6 is added to generate a carry bit and cause the sum to
become a valid entry. The reason for adding 6 is that there are 16 possible 
4-bit BCD values (since 2​ 4​ = 16),
but only 10 values are valid (0000 through 1001).

Authors:
--------

Abdel-aziz Abdel-naser    20140168  CS_IS_2
Abdullah Abdel-meneim     20140171  CS_IS_2

"""


def adding_BCD(num1, num2):
    def complete_4(bcd):
        while len(bcd) % 4 != 0:
            bcd = '0' + bcd
        return bcd

    def make_same_lenght(x1, x2):
        while len(x1) > len(x2):
            x2 = '0' + x2
        while len(x2) > len(x1):
            x1 = '0' + x1
        return x1, x2

    def int_to_BCD(num):
        bcd = int(str(num), 16)
        return complete_4(bin(bcd).replace('0b', ''))

    def BCD_to_int(bcd):
        complete_4(bcd)
        num = ''
        while len(bcd) > 0:
            num += str(int(bcd[0:4], 2))
            bcd = bcd[4:]
        return int(num)

    def add(x1, x2, x3=0):
        x1 = int(x1, 2)
        x2 = int(x2, 2)
        if x1 + x2 + x3 > 9:
            return bin((x1 + x2 + x3 + 6)).replace('0b', '')[1:], 1
        else:
            return bin(x1 + x2 + x3).replace('0b', ''), 0
    num1_bcd = int_to_BCD(num1)
    num2_bcd = int_to_BCD(num2)
    num1_bcd, num2_bcd = make_same_lenght(num1_bcd, num2_bcd)
    print(num1_bcd, "\t\t(%d)" % num1)
    print('+')
    print(num2_bcd, "\t\t(%d)" % num2)
    print('__________________________')

    num1_bcd = num1_bcd[::-1]
    num2_bcd = num2_bcd[::-1]
    c = 0
    result = ''
    while len(num1_bcd) > 0:
        n1 = num1_bcd[0:4]
        n2 = num2_bcd[0:4]
        n1 = n1[::-1]
        n2 = n2[::-1]
        r, c = add(n1, n2, c)
        result = str(r) + result
        num1_bcd = num1_bcd[4:]
        num2_bcd = num2_bcd[4:]

    result = str(c) + result
    result = complete_4(result)

    print(result, "\t\t(%d)" % BCD_to_int(result))


if __name__ == '__main__':
    print("Enter the first number")
    num1 = int(input())
    print("Enter the second number")
    num2 = int(input())
    adding_BCD(num1, num2)
