#!/usr/bin/env python3
# Author ID: [seneca_id]

def is_digits(sobj):
    # place code here - loop through each character in sobj 
    intergers_test = {'0','1','2','3','4','5','6','7','8','9'}
    #had to convert to individual characters to work, tried as single string '0123456789' and could not get it working
    for string in sobj:
        if string not in intergers_test:
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')