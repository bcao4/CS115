'''
Created on Sep 12, 2018

@author: brandon
'''

'''
Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System
'''

def dot(L, K):
    '''returns the dot product of the lists L and K'''
    if L==[] or K==[]:
        return 0.0
    return L[0]*K[0] + dot(L[1:], K[1:])

def explode(s):
    ''' return a list of the characters in that string'''
    if s=="":
        return []
    return [s[0]] + explode(s[1:])

def ind(e, L):
    ''' returns the index at which e is first found in L'''
    if L==[] or L=="":
        return 0
    if e == L[0]:
        return 0
    return 1 + ind(e, L[1:])

def removeAll(e, L):
    '''return a list that is identical to L except that all elements identical to e have been removed'''
    if L==[]:
        return []
    if e==L[0]:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])

def even(X):
    '''returns if a number is even or not'''
    if X % 2 == 0 : return True 
    else: return False
    
def myFilter(e, L):
    '''returns a new list that contains all of the elements of L'''
    if L==[]:
        return []
    if e(L[0])==True:
        return [L[0]] + myFilter(e, L[1:])
    return myFilter(e, L[1:])
    
    
def deepReverse(L):
    '''takes as input a list of elements and returns the list in reverse order'''
    if L==[]:
        return []
    if isinstance (L[0], list):
        return deepReverse(L[1:])+[deepReverse(L[0])]
    return deepReverse(L[1:]) + [L[0]]


print(explode("Spam"))
print(dot([5,3], [6,4]))
print(ind(42,[55, 77, 42, 12, 42, 100]))
print(removeAll(42, [55, 77, 42, 11, 42, 88]))
print(myFilter(even, [0, 1, 2, 3, 4, 5, 6]))
print(deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]))
