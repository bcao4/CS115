'''
Created on Oct 10, 2018
@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    return numToBinary(n//2) + str(n%2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    elif s[0]=='0':
        return binaryToNum(s[1:])
    elif s[0]=='1':
        return ((2**(len(s)-1)) + binaryToNum(s[1:]))
    
def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s=='11111111':
        return '00000000'
    return ('00000000' + numToBinary(binaryToNum(s)+1))[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n==0:
        return ''
    return count(increment(s),n-1)
    
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    return numToTernary(n//3) + str(n%3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    elif s[0]=='0':
        return ternaryToNum(s[1:])
    elif s[0]=='1':
        return ((3**(len(s)-1)) + ternaryToNum(s[1:]))
    elif s[0]=='2':
        return ((3**(len(s)-1))*2 + ternaryToNum(s[1:]))
    
#print(isOdd(42))
#print(numToBinary(13))
#print(binaryToNum('1001101'))
#print(increment('00000000'))
#print(count('00000000', 4))
#print(numToTernary(42))
#print(ternaryToNum('22'))