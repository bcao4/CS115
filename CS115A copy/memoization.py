'''
Created on Oct 1, 2018

@author: brandon
'''
import time

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

start_time= time.time()
#print(fib(40))
#print('fib computation time without memoization: %.2f' % (time.time()-start_time))

def fib_memo(n):
    def fib_helper(n,memo):
        #if key is in memo, return memo[n]
        if n in memo:
            return memo[n]
        #Do work!
        #Recursively compute the next fibonaci number
        #Store the result in a local variable
        if n<=1:
            result=n
        else:
            result = fib_helper(n-1, memo) + fib_helper(n-2, memo)
            
            #Store result in memo and return result
        memo[n] = result
        return result
    return fib_helper(n,{})
    
start_time= time.time()
#print(fib_memo(40))
#print('fib_memo computation time with memoization: %.2f' % (time.time()-start_time))

def LCS(s1, s2):
    '''returns the length of the longest common subsequence in strings s1 and s2'''
    if s1=='' or s2=='':
        return 0
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:],s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))    


def LCS_memo(s1,s2):
    def LCS_helper(s1,s2,memo):
        if (s1,s2) in memo:
            return memo[(s1,s2)]
        if s1=='' or s2=='':
            result=0
        elif s1[0] == s2[0]:
            result= 1 + LCS_helper(s1[1:],s2[1:], memo)
        else:
            result= max(LCS_helper(s1, s2[1:],memo), LCS_helper(s1[1:], s2, memo))
        memo[(s1,s2)]=result
        return result
    return LCS_helper(s1,s2,{})

def LCS_with_values(s1, s2):
    if s1=='' or s2=='':
        return [0, '']
    if s1[0]==s2[0]:
        result = LCS_with_values(s1[1:], s2[1:])
        return [1 + result[0], s1[0] + result[1]]
    useS1 = LCS_with_values(s1, s2[1:])
    useS2 = LCS_with_values(s1[1:], s2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2

def fast_LCS_with_values(s1, s2):
    def fastLCS_helper(s1,s2,memo):
        if (s1,s2) in memo:
            return memo[(s1,s2)]
        if s1=='' or s2=='':
            result=[0,'']
        elif s1[0]==s2[0]:
            lose_both = fastLCS_helper(s1[1:], s2[1:],memo)
            result= (1 + lose_both[0], s1[0] + lose_both[1])
        else:
            useS1 = fastLCS_helper(s1, s2[1:], memo)
            useS2 = fastLCS_helper(s1[1:] ,s2, memo)
            if useS1[0] > useS2[0]:
                result= useS1
            else:
                result= useS2
        memo[(s1,s2)] = result
        return result
    return fastLCS_helper(s1, s2, {})

def subset(target, lst):
    '''determines whether or not it is possible to create target sum using the values in the list. 
    Values in the list can be positive, negative or zero.'''
    if target==0:
        return True
    if lst==[]:
        return False
    return subset(target-lst[0],lst[1:]) or subset(target, lst[1:])

def fastSubset_helper(target, lst):
    def fastSubset_helper(target, lst, memo):
        if (target, lst) in memo:
            return memo[(target, lst)]
        if target==0:
            result= True
        elif lst==[]:
            result= False
        
            
    
    
    
start_time= time.time()
print(fast_LCS_with_values('sefhegewrdwfesthefvsefjesjfh','efgewgwegsrgthecstgrbse'))
print('fast_LCS_with_values computation time with memoization: %.2f' % (time.time()-start_time))
