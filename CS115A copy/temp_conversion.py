'''
Created on Aug 31, 2018

@author: brandon
'''

"""
Put the function at the top of program
"""

def celsius(fahrenheit):
    """returns the input Fahrenheit degrees in Celsius"""
    return 5/9 + (fahrenheit - 32)
    
def fahrenheit(celsius):   
    """Returns the input Celsius degrees in Fahrenheit"""
    return 9 / 5 * celsius + 32 

"""
Call the functions below the function definitions
"""

c= float(input('Enter degrees in Celsius: '))
f = fahrenheit(c)
# You can print multiple items in one statement. If you put a comma after each
#item, it prints a space and then foes on to print the next item.
print(c, 'C =', f, 'F') 
#You can print this way too, but allowing exactly two decimal places. 
print('%.2f C = %.2f F' % (c,f)) 

f= float(input('Enter degrees in Fahrenheit: '))
c = celsius(f)
print(f, 'F =', c, 'C') 
print('%.2f F = %.2f C' % (f,c)) 

"""
Try composition of funcstions.
Converting a fahrenheit temperature to Celsius and back to fahrenheit should 
give the original fahrenheit temperature.
"""

print() #print by itself prints a new line
f= float(input('Enter degrees in Fahrenheit: '))

#User assert to check the returned value is equal to the expected value
assert fahrenheit(celsius(f)) 
#No output should be produced, unless the assertion fails, which means you
#have an error (either in your code or your expectation). 

