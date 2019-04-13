'''
Created on Apr 20, 2012

@author: bribor
'''
from rectangle2 import Rectangle2

class Square2(Rectangle2):
    def __init__(self, x, y, length, name="Square"):
        super().__init__(x, y, length, length, name)

    @Rectangle2.length.getter
    def length(self):
        return self._Rectangle__length

    @length.setter
    def length(self, length):
        self._Rectangle__length = length
        self._Rectangle__width = length

    @Rectangle2.width.getter
    def width(self):
        raise AttributeError("Square has no attribute 'width'.")

    @width.setter
    def width(self, width):
        raise AttributeError("Square has no attribute 'width'.")

if __name__ == '__main__':
    sqr = Square2(10, 10, 20)
    sqr.length = 50
    print(sqr)
    print(sqr.length)
