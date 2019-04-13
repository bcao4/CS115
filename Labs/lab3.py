'''
Created on Sep 18, 2018

@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
'''

def change(amount, coins):
    '''returns the least number of coins that makes up that amount of money'''
    if amount==0:
        return 0
    if coins==[] or 0>amount:
        return float('inf')
    use_it= 1 + change(amount-coins[0], coins)
    lose_it= change(amount, coins[1:])
    return min(use_it, lose_it)

print(change(48, [1, 5, 10, 25, 50]))
