#!/usr/bin/python3
"""Rectangle module
This module defines a Rectangle class
"""


class Rectangle:
    """Rectangle class
    this is the class for rectangle
    """

    def __init__(self, width=0, height=0):
        """__init__ method
        this method initializes on instance creation
        """
        self.height = height
        self.width = width

    def __str__(self):
        """__str__ method
        this method will print the rectangle on print() or str()
        """
        my_str = ""
        if self.__width == 0 or self.__height == 0:
            return my_str
        for i in range(self.__height):
            for j in range(self.__width):
                my_str += '#'
            if i is not (self.__height - 1):
                my_str += "\n"
        return my_str

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area Method
        this method will calculate the rectangle object's area
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter Method
        this method will calculate the rectangle object's perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __repr__(self):
        """
        Returns the representation of the Rectangle.
        """
        strWidth = str(self.width)
        strHeight = str(self.height)
        return f"Rectangle({strWidth}, {strHeight})"

    def __del__(self):
        """__del__
        executes upon object deletion
        """
        print("Bye rectangle...")
