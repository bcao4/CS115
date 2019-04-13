'''
Created on Sep 26, 2018

@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
'''

def knapsack(capacity, itemList):
    ''' returns both the maximum value and the list of items that make this value, without exceeding the capacity of your knapsack'''
    if capacity==0 or itemList==[]:
        return [0, []]
    if itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    use_it= knapsack(capacity-itemList[0][0], itemList[1:])
    lose_it= knapsack(capacity, itemList[1:])
    newsum= itemList[0][1]+use_it[0]
    if newsum>lose_it[0]:
        return [newsum, [itemList[0]]+use_it[1]]
    return lose_it
        
    

   

print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
    
        
    