'''
Created on Sep 10, 2018

@author: brandon
'''
from cs115 import map, range, reduce, filter
import math

def factorial(n):
    if n== 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def tower(n):
    '''computes 2^(2^(2...))) using recursions'''
    if n==0:
        return 1
    return 2 ** tower(n-1)

print(map(tower, range(5)))

def tower_reduce(n):
    '''computes 2^(2^(2...))) using reduce'''
    def power(y, x):
        return x**y
    return reduce(power, [2] * n)

print(map(tower_reduce, range(1,5)))

def length(lst):
    '''returns the length of the list'''
    if lst == []:
        return 0
    return 1 + length(lst[1:])

print(length([1,2,3,2,7]))

def length_str(s):
    '''returns the length of the string'''
    if s == "":
        return 0
    return 1+ length_str(s[1:])

def reverse(lst):
    '''takes as input a list of elements and returns the list in reverse order'''
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]]

print(reverse([1,2,3,4,5]))

def member(x, lst):
    '''returns true if x is contained in the list, and false otherwise'''
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])

def collapse(lst):
    '''collapses a list of possible nested lists into a single list of values'''
    if lst == []:
        return []
    if isinstance(lst[0], list):
        return collapse(lst[0]) + collapse(lst[1:])
    return [lst[0]] + collapse(lst[1:])

print (collapse ([1, [2, [3, 4]], 5]))

def my_map(f, lst):
    '''return a new list where the function has been applied to every element in the original list'''
    if lst==[]:
        return []
    return [f(lst[0])] + my_map(f, lst[1:])

def power(x, y):
    '''returns x^y'''
    if y==0:
        return 1
    return x * (x, y-1)

def power_tail(x, y):
    '''computes x^y using tail recursion'''
    def power_tail_helper(x,y,accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y-1, accum*x)
    return power_tail_helper(x, y, 1)

def sqr(x):
    return x*x
    
print(my_map(sqr, [1,2,3]))

def my_reduce(f, lst):
    '''reduces a list to a single value as dictated by the predicate f'''
    def my_reduce_helper(f, lst, accum):
        if lst==[]:
            return accum
        return my_reduce_helper(f, lst[1:], f(accum, lst[0]))
    if lst==[]:
        raise TypeError('my_reduce() of empty sequence with no initial value')
    return my_reduce_helper(f, lst[1:], lst[0])

def add(x,y):
    return x+y

print(my_reduce(add, range(11)))

def prime(n):
    '''returns whether or not an integer is prime'''
    possibleDivisors = range(2, int(math.sqrt(n))+ 1)
    divisors=filter(lambda x: n%x==0, possibleDivisors)
    return len(divisors)==0

def primes(n):
    def sieve(lst):
        if lst==[]:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n+1))

print(primes(100))

def fib(n):
    if n==0 or n==1: #if n<=1
        return n
    return fib(n-1) + fib(n-2)

def subset(target, lst):
    '''determines whether or not it is possible to create target sum using the values in the list. 
    Values in the list can be positive, negative or zero.'''
    if target==0:
        return True
    if lst==[]:
        return False
    return subset(target-lst[0],lst[1:]) or subset(target, lst[1:])

print(subset(5, [3,1,2]))

def powerset(lst):
    '''returns the powerset of the list, that is, the set of all subsets of the list.'''
    if lst==[]:
        return [[]]
    lose_it= powerset(lst[1:])
    use_it= map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it

print(powerset([1,2,3]))

def subset_with_values(target, lst):
    '''determines whether or not it is possible to create the target sum using values in the list 
    (can be negative, positive or zero). The function returns a tuple of exactly 2 items. The first is a
    Boolean that indicates True (if the sum is possible and False if it' s not). The second element in the 
    tuple is a list of all the values that add up to make that target sum.'''
    if target==0:
        return (True, [])
    if lst==[]:
        return (False, [])
    use_it= subset_with_values(target-lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]]+use_it[1])
    return subset_with_values(target, lst[1:])

print(subset_with_values(5,[1,2,3]))

def LCS(s1, s2):
    '''returns the length of the longest common subsequence in strings s1 and s2'''
    if s1=='' or s2=='':
        return 0
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:],s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))    

print(LCS('spot', 'pot'))
print(LCS('maps', 'spasm'))

def LCS_with_values(s1, s2):
    if s1=='' or s2=='':
        return [0, '']
    if s1[0]==s2[0]:
        result = LCS_with_values(s1[1:], s2[1:])
        return [1 + result[0], s1[0] + result[1]]
    useS1 = LCS_with_values(s1, s2[1:])
    useS2 = LCS_with_values(s1[1:], s2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2

print(LCS_with_values('spot', 'pots'))

def coin_row(lst):
    if lst==[]:
        return 0
    return max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))

def coin_row_with_values(lst):
    if lst==[]:
        return [0, []]
    use_it= coin_row_with_values(lst[2:])
    new_sum= lst[0] + use_it[0]
    lose_it= coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]]+ use_it[1]]
    return lose_it

def distance(first, second):
    if first=='':
        return len(second)
    if second=='':
        return len(first)
    if first[0]==second[0]:
        return distance(first[1:], second[1:])
    substitution= 1 + distance(first[1:], second[1:])
    insertion = 1 + distance(first, second[1:])
    deletion= 1 + distance(first[1:], second)
    return min(substitution, insertion, deletion)
                                      
print(coin_row([]))
print(coin_row_with_values([]))
print(coin_row([5, 1, 2, 10, 6, 2]))
print(coin_row_with_values([5, 1, 2, 10, 6, 2]))
print(coin_row([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))
print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

print(distance('sam', 'am'))
print(distance('pot', 'spatty'))
    
    
    