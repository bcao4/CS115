'''
Created on Sep 24, 2018
@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System. 
CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    '''returns the least number of coins that makes up that amount of money and the list of the coins'''
    if amount==0:
        return [0,[]]
    if coins==[] or 0>amount:
        return [float('inf'),[]]
    use_it= giveChange(amount - coins[-1], coins)
    lose_it= giveChange(amount, coins[:-1])
    if use_it[0] < lose_it[0]:
        return [1 + use_it[0], [coins[-1]] +use_it[1]]
    return lose_it

def giveChanges(amt,coins):
    if amt==0:
        return [0,[]]
    if coins==[]:
        return [float('inf'),[]]
    if coins[0]>amt:
        return giveChanges(amt,coins[1:])
    useit=giveChanges(amt-coins[0], coins)
    loseit=giveChanges(amt,coins[1:])
    newsum=1+useit[0]
    if newsum<loseit[0]:
        return [newsum, [coins[0]]+useit[1]]
    return loseit

print(giveChanges(48, [1, 7, 24, 42]))

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    '''returns a value associated with the given letter'''
    if scorelist==[]:
        return 0
    if letter==scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])
                               
def wordScore(S, scorelist):
    '''returns the scrabble score of that string'''
    if scorelist== []:
        return []
    if S=="":
        return 0
    return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct==[]:
        return []
    return[[dct[0],wordScore(dct[0],scores)]] + wordsWithScore(dct[1:],scores)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n==0:
        return []
    if n>len(L):
        return L
    return [L[0]]+take(n-1, L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n==0:
        return L
    if L==[] or n>=len(L):
        return []
    if n==1:
        return L[1:]
    return drop(n-1, L[1:])


print(wordsWithScore(['dog','cat','mouse','test'],scrabbleScores))
print(take(4,[1,4,7,35,7,3,4]))
print(drop(3,[1,4,7,35,7,3,4]))


