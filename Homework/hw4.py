'''
Created on Oct 2, 2018

@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
'''
def pascal_helper(lst):
    ''' returns a new list of sums of adjacent terms in the original list'''
    if lst==[]:
        return []
    if lst==[1]:
        return [1]
    return ([lst[0]+lst[1]])+ pascal_helper(lst[1:])

def pascal_row(n):
    ''' returns a list of elements found in a certain row of Pascal’s Triangle.'''
    if n==0:
        return [1]
    if n==1:
        return [1,1]
    return [1]+ pascal_helper(pascal_row(n-1))

def pascal_triangle(n):
    '''returns a list of lists containing the values of the all the rows up to and including row n'''
    if n==0:
        return[[1]]
    return pascal_triangle(n-1) + [pascal_row(n)]


print(pascal_helper([1,3,3,1]))
print(pascal_row(2))
print(pascal_triangle(5))