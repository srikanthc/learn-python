#! /usr/bin/env python

# This program sums given integers/floats as command line parameters
import sys

def my_sum(numbers):
    sum = 0
    if numbers:
        for number in numbers:
            sum += number
    return sum

if __name__ == '__main__':
    sum = my_sum(float(num) for num in sys.argv[1:])
    print 'Sum of given numbers is ', sum
            
