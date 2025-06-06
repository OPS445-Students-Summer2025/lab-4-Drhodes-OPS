#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(five_chars):
    # Place code here - refer to function specifics in section below
    firstchar_string = five_chars[0:5]
    return firstchar_string

def last_seven(lastseven_chars):
    # Place code here - refer to function specifics in section below
    end_of_string = lastseven_chars[-7:]
    return end_of_string

def middle_number(num):
    # Place code here - refer to function specifics in section below
    convstr = str(num)
    second_third = convstr[1:3]
    return second_third

def first_three_last_three(x,y):
    # Place code here - refer to function specifics in section below
    first_last = x[:3] + y[-3:]
    return first_last


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))