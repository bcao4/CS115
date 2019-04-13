'''
Created on Oct 29, 2018

@author: brandon
'''
import random
import time

def map_sqr(lst):
    '''assume lst is a list. return map(sqr, lst)'''
    result=[]
    for x in lst:
        result.append(x * x)
    return result

def map_sqr_list_comprehension(lst):
    '''assume lst is a list. return map(sqr, lst)'''
    return [x*x for x in lst]

def find_max(lst):
    '''returns the maximum element in the list'''
    if lst==[]:
        return None
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

def find_min_max(lst):
    '''returns a tuple of both the min and max values in the list'''
    if lst==[]:
        return None
    max_val = min_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val=x
        elif x < min_val:
            min_val = x
    return (min_val, max_val)

def shallow_copy(lst):
    new_list = []
    for x in lst:
        new_list.append(x)
    return new_list

def shallow_copy_list_comprehension(lst):
    return [x for x in lst]

#L=[1,2,[3,[4,5]]]
#M=shallow_copy(L)
#L[2]=1
#print(M)

def deep_copy(lst):
    new_list = []
    for x in lst:
        if type(x) is list:
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list

L=[1,2,[3,[4,5]]]
M=deep_copy(L)
L[2][1][0] = 14
#print(M)
#print(L)

# char='C'
# for i in range(1,6):
#     if i%3==0:
#         char='A'
#     elif i%2==0:
#         char='B'
    #print(char * i)
    
def sequential_search(key, lst): 
    '''returns the index of key in lst, if it exists, andd -1 otherwise''' 
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

def binary_search(lst, key):
    '''searches the lst for key'''
    low = 0
    high= len(lst)-1
    while high>=low:
        mid= low+(high-low) // 2
        if key < lst[mid]:
            high=mid-1
        elif key>lst[mid]:
            low=mid+1
        else:
            return mid
    return -low-1

def mean(lst):
    '''prints average of a list'''
    total=0
    for x in lst:
        total += x
    return total/len(lst)
#i=0
#while True:
    #i += 1
    #if i == 3:
        #continue
    #print(i)
    
def swap(lst, a, b):
    '''swaps lst[a] with lst[b]'''
    temp=lst[a]
    lst[a]=lst[b]
    lst[b]=temp

#selection sort always makes (n(n-1))/2 comparisons
#makes at most n-1 swaps

def selection_sort(lst):
    n=len(lst)
    for i in range(n-1):
        min_index=i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            swap(lst, i, min_index)
    return min_index
        
def num_matches(list1, list2):
    '''returns the number of elements that the two lists in common'''
    list1.sort()
    list2.sort()
    matches= i = j= 0
    while i < len(list1) and j < len(list2):
        if list1[i]==list2[j]:
            matches+=1
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else: j+=1
    return matches
    
def keep_matches(list1, list2):
    '''returns a list of the elements that the two lists have in common'''
    list1.sort()
    list2.sort()
    result=[]
    i = j= 0
    while i < len(list1) and j < len(list2):
        if list1[i]==list2[j]:
            result.append(list1[i])
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else: 
            j+=1
    return result
    
def drop_matches(list1, list2):
    '''returns a new list that contains only the elements in list2 that are 
    not in list1'''
    list1.sort()
    list2.sort()
    result=[]
    i = j= 0
    while i < len(list1) and j < len(list2):
        if list1[i]==list2[j]:
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else: 
            result.append(list2[j])
            j+=1
    while j < len(list2):
        result.append(list2[j])
        j+=1
    return result    
   
A=[2,3,5,7,9,11,13,17,23]
B=[11,13,15,17,19,21,23,25,27]
print(num_matches(A, B))  
print(keep_matches(A, B))

# random_list= [random.randint(1,100000) for _ in range(20000)]
# copy_list= list(random_list)
# 
# start = time.clock()
# selection_sort(random_list)
# print('Elasped time: %.2f seconds' % (time.clock() - start))
# print(selection_sort([5,2,6,1,8]))

#print(map_sqr([1,2,3]))
#print(map_sqr_list_comprehension([1,2,3]))
#print(find_max([1,3,4,6,7]))
#print(find_min_max([4,3,7,1,10]))