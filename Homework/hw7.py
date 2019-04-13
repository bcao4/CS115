'''
Created on Oct 21, 2018
@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
'''

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

def baseToBase(B1,B2,SinB1):
    '''takes a string SinB1 that is in base B1, and returns a string in base B2,
    both bases of which are between 2 and 10, inclusive'''
    return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S,T):
    '''two binary strings S and T as input and returns their sum, also in binary'''
    return numToBaseB((baseBToNum(S, 2) + baseBToNum(T, 2)), 2)

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = { 
('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') 
}

def addBhelper(S, T):
    '''returns the carry of bits in binary'''
    if S=='' or T=='':
        return '0'
    if S=='0' or T=='0':
        return '0'
    return '1'
    
def addB(S,T):
    '''return a new string representing the sum of the two input strings. The sum
    is computed using the binary addition algorithm'''
    if T=='':
        return S
    if S=='':
        return T
    return addB(S[:-1],T[:-1])+FullAdder[S[-1],T[-1], addBhelper(S[-1],T[-1])] [0]

print(numToBaseB(0, 4))
print(baseBToNum("2110", 3))
print(baseToBase(3, 5, "11"))
print(add("110", "011"))
print(addB("011", "100"))
