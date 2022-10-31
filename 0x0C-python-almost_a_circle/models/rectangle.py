#!/usr/bin/python3
""" rectangle module """
from models.base import Base

class Rectangle(Base):
    """ rectangle class """
    __width = None
    __height = None
    __x = None
    __y = None

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Private instance

        args:
            id:id
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        Base.strict_integer("width", width)
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        Base.strict_integer("height", height)
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        Base.integer_validation("x", x)
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        Base.integer_validation("y", y)
        self.__y = y

    def area(self):
        """
        Function that returns area of rectangle
        """
        return self.height * self.width

    def display(self):
        """
        Functions that prints the rectangle instance in stdout
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Function that return a string representation of the rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, *args, **kwargs):
        return self.id, self.width, self.height, self.x, self.y(args, kwargs)
