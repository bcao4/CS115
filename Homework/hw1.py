'''
Created on Sep 6, 2018

@author: brandon
'''

'''
Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System
'''

from cs115 import reduce, map, range

def add(x, y):
    '''returns the sum of x and y'''
    return x + y

def mult(x, y):
    '''returns the product of x and y'''
    return x * y

def factorial(n):
    '''returns the factorial of n'''
    return reduce(mult, range(1, n+1))

def mean(L):
    '''returns the average of a list of numbers'''
    return reduce(add, L)/(len(L))

def divides(n):
    def div(k):
        return n % k == 0
    return div

def prime(n):
    '''checks if a number is prime or composite'''
    return (sum(map(divides(n), range(2, n))) == 0)

print(factorial(5))
print(mean([1,2,3,4]))
print(prime(11))


