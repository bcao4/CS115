'''
Created on Sep 13, 2018
@author: Brandon Cao
Username: bcao4
I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    if scorelist==[]:
        return 0
    if letter==scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])
                               
def wordScore(S, scorelist):
    if scorelist== []:
        return []
    if S=="":
        return 0
    return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)

def list_of_words(dict, RACK):
    return filter(lambda word: isPossible(word, RACK), dict)

def remove(letter, RACK):
    if letter==RACK[0]:
        return RACK[1:]
    return [RACK[0]] + remove(letter, RACK[1:])
    
def isPossible(word, RACK):
    if word=="":
        return True
    if word[0] in RACK:
        return isPossible(word[1:],remove(word[0], RACK))
    return False

def scoreList(RACK):
    return map(lambda word: [word, wordScore(word,scrabbleScores)], list_of_words(Dictionary, RACK))

def bestWord(RACK):
    scorelist=scoreList(RACK)
    if scorelist==[]:
        return["",0]
    return reduce(lambda x,y: x if x[1]>y[1] else y, scorelist)

print(bestWord(["a", "s", "m", "t", "p"]))