'''
Created on Sep 5, 2018

@author: brandon
'''

'''Brandon Cao
bcao4
I pledge my honor that I have abided by the stevens honor system.'''

from cs115 import map, reduce, range
import math

def inverse(n):
    '''returns the inverse of n'''
    return float(1/n)

def add(x,y):
    '''Returns the sum of x and y'''
    return x+y

def e(n):
    '''returns approximated value of e'''
    return 1 + reduce(add, map(inverse, map(math.factorial, range(1, 1+n))))

def error(n):
    '''returns the absolute value of the difference between the actual value of e 
    and the approximated value of e'''
    return abs(math.e-e(n))

print(inverse(3))
print(e(10))
print (error(10))