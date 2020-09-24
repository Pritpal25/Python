# this import is only required in python version < 3
from __future__ import print_function

# OUTPUT
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='*', end='end')
print()

x = 2; y = 3
print('The value of x is {} and value of y is {}'.format(x,y))

print('I love {0} and {1}'.format('bread', 'butter'))
print('I love {1} and {0}'.format('bread', 'butter'))
print('Hello {name}, {greeting}'.format(name = 'Maneet', greeting = 'Good, Morning'))


x = 12.12343432
print('Value of x is %3.2f' %x)
print('Value of x is %3.4f' %x)


# INPUT
num = input('Enter a number\n') # message is optional
print(type(num)) # was expected to be string, but is an int
num = int(num)
print(type(num)) # int type

print(eval('2+3')) #type casting for expressions doesnt work, use eval for that
#print(int('2+3')) - throws error

# IMPORT

import math # importing a library
print(math.pi)

from math import pi # selectively importing things from library
print(pi)

import sys
print(sys.path) # all the locations where python looks for import
