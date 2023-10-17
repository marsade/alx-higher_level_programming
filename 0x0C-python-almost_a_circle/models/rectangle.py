#!/usr/bin/python3
"""First Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a new Rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """returns x value"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """return y value"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
