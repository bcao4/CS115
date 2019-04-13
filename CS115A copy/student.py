'''
Created on Nov 12, 2018

@author: brandon
'''
# A class is a collection of attributes (fields or even properties) 
# and a set of methods that change the value of the attributes.
# It's blueprint for defining objects that you wish to model
# in code. A class has a constructor, a special method called
# __init__, whose purpose is to initialize the instance variables
# of the object being created

# public instance variable- no underscores
# private- 2 underscores
# protected- 1 underscore

class Student(object):
    def __init__(self, first_name, last_name, sid, gpa):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__sid = sid 
        self.__gpa = gpa 
        
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
        
    def __stir__(self):
        return self.__first_name + ' ' + self.__last_name + '(SID:' + \
            self.__sid  + ', GPA:' + str(self.__gpa) + ')'
            

if __name__== '__main__':
    s1 = Student('Brian', 'Borowski', '12345', 4.0)
    print(s1.first_name)
    s1.first_name = 'Scott'
    print(s1.first_name)
    print(s1)