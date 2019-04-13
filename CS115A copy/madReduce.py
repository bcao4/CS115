'''
Created on Sep 5, 2018

@author: brandon
'''
from cs115 import map, reduce, range

def add(x,y):
    '''Returns the sum of x and y'''
    return x+y

def square(x):
    '''Returns the square of x'''
    return x * x

def mult(x, y):
    '''Returns the product of x and y'''
    return x * y

def span(lst):
    '''Returns the difference between the maximum and minimum numbers in a list'''
    return reduce(max, lst) - reduce(min, lst)

def gauss(n):
    '''takes as input a positive integer n and returns the sum
    1+2+3+...+n'''
    return reduce(add, range(1, n+1))
    
def sum_of_squares(n):
    '''Takes as input a positive integer n and returns the sum 1^2 + 2^2 + 3^2 + ... + n^2'''
    return reduce(add, map(square, range(1, n+1)))

print (span([3, 1, 42, 7]))
print (span([42, 42, 42, 42]))
print (gauss(10))
print (sum_of_squares(10))

list_of_ints = [1, 2, 3, 4, 5]
print(reduce(mult, list_of_ints))

list_of_strings = ['hello', 'my', 'name', 'is', 'brian']
print (reduce(max, map(len, list_of_strings)))