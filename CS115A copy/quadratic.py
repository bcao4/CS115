'''
Created on Nov 14, 2018
@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
'''

import math

class QuadraticEquation(object):
    '''a class that represents quadratic equations'''
    def __init__(self,a,b,c):
        self.__a=float(a)
        self.__b=float(b)
        self.__c=float(c)
        if a==0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
    
    @property
    def a(self):
        return self.__a
   
    @property
    def b(self):
        return self.__b
            
    @property
    def c(self):
        return self.__c
    
    def discriminant(self):
        '''returns the discriminant for the given values'''
        return (self.__b**2)-(4*self.__a*self.__c)
        
    def root1(self):
        '''returns one root'''
        if self.discriminant()<0:
            return None
        return ((-self.__b)+(math.sqrt(self.discriminant()))) / (2*self.__a)
    
    def root2(self):
        '''returns the other root'''
        if self.discriminant()<0:
            return None
        return ((-self.__b)-(math.sqrt(self.discriminant()))) / (2*self.__a)
    
    def __str__(self):
        '''returns a string representation of the quadratic equation'''
        _a = str(self.__a)
        _b = str(self.__b)
        _c = str(self.__c)
        
        if self.__a==1.0:
            _a='x^2'
        if self.__a==-1.0:
            _a='-x^2'
        if self.__a>0 and self.__a!=1 and self.__a!=-1:
            _a=_a+'x^2'
        if self.__a<0 and self.__a!=1 and self.__a!=-1:
            _a='-' + _a[1:]
            
            
        if self.__b==1.0:
            _b=' + x'
        if self.__b==-1.0:
            _b=' - x'
        if self.__b>0 and self.__b!=1 and self.__b!=-1:
            _b=' + ' + _b + 'x'
        if self.__b<0 and self.__b!=1 and self.__b!=-1:
            _b=' - ' + _b[1:] + 'x'
        if self.__b==0:
            _b=''     
        
        
        if self.__c==1.0:
            _c=' + 1.0'
        if self.__c==-1.0:
            _c=' - 1.0'
        if self.__c>0 and self.__c!=1 and self.__c!=-1:
            _c=' + ' + _c
        if self.__c<0 and self.__c!=1 and self.__c!=-1:
            _c= ' - ' + _c[1:] + ''
        if self.__c==0:
            _c=''
        
        return _a+_b+_c+' = 0'