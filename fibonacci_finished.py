#!/usr/bin/env python

# import some modules so that we get some extra functionality
import os


def do_fibonacci(fir, sec):
    print(fir)
    temp = sec
    sec += fir
    fir = temp
    return fir, sec


# clear the console screen
os.system('clear')

# ask for the option they would prefer
msg = '''What is your preference:
1. nth Fibonacci number
2. last Fibonacci number <= n
'''
option = int(input(msg))

# only continue if you recognize their choice
if option == 1 or option == 2:
    # ask for the n
    n = int(input("\nPlease enter the number: "))
    # keep track of the current first and second numbers
    first = 0
    second = 1
    # switch on their choice for separate algorithms
    if option == 1:
        # for option 1, loop for n times
        for i in range(n):
            first, second = do_fibonacci(first, second)
            # print first,
            # temp = second
            # second += first
            # first = temp
        # print the answer
        print('\nThe answer is: ' + str(first))
    elif option == 2:
        # loop while we are <= to n
        while second <= n:
            first, second = do_fibonacci(first, second)
            # print first,
            # temp = second
            # second += first
            # first = temp
        # print the answer
        print('\nThe answer is: ' + str(first))
else:
    print("I didn't understand your option")


# wait for the user to press enter to quit
input('\nPress enter to quit...')

# clear the console screen
os.system('clear')
