'''
Created on Oct 30, 2018
@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
'''

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
    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])

def numToBaseB(N, B):
    '''takes as input a non-negative integer N and a base B 
    (between 2 and 10 inclusive) and returns a string representing the number N in
    base B'''
    if N==0:
        return ''
    return numToBaseB(N//B, B) + str(N%B)

def baseBToNum(S, B):
    '''takes a string S of base B and returns the integer value'''
    if S == '':
        return 0
    return baseBToNum(S[:-1],B) * B + int(S[-1])

def add(S,T):
    '''two binary strings S and T as input and returns their sum, also in binary'''
    return numToBaseB((baseBToNum(S, 2) + baseBToNum(T, 2)), 2)

def convert(s):
    if s=='':
        return ''
    if s[0]=='1':
        return '0' + convert(s[1:])
    return '1' + convert(s[1:])

def padder(s):
    """returns a 8bit string"""
    if len(s) >= 8:
        return s[-8:]
    return padder('0'+s)

def TcToNum(n):
    '''takes as input a string of 8 bits representing an integer 
    in two's-complement, and returns the corresponding integer'''
    if n[0]=='1':
        return -1* binaryToNum(convert(add(n,'11111111')))
    return binaryToNum(n)

def NumToTc(n):
    '''takes as input an integer N, and returns a string
    representing the two's-complement representation of that integer.'''
    if n>=128 or n<-128:
        return 'Error'
    if n>=0:
        return padder(numToBinary(n))
    return add(convert(padder(numToBinary(n*-1))),'1')
        

print(convert('100010'))
print(padder('10111'))
print(TcToNum('10000000'))
print(NumToTc(-9))