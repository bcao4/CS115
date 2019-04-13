'''
Created on Apr 19, 2012

@author: bribor
'''
from shape import Shape

class Rectangle2(Shape):
    def __init__(self, x, y, length, width, name="Rectangle"):
        super().__init__(x, y, name)
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, length):
        self._length = length

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def area(self):
        return self._length * self._width

    def __str__(self):
        return super().__str__() + ", length = " + \
            str(self._length) + ", width = " + str(self._width) + \
            ", area = " + str(self.area)

if __name__ == '__main__':
    rect = Rectangle2(10, 10, 20, 20)
    print(rect)
    rect.x = 30
    rect.y = 30
    print(rect)
    rect.length = 100
    rect.width = 200
    print(rect)

    print(isinstance(rect, Rectangle2))
    print(isinstance(rect, Shape))
    print(isinstance(rect, object))
    print(isinstance(rect, str))
