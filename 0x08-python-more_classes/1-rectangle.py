#!/usr/bin/python3
# 1-rectangle.py
"""Defines rectangle class"""


class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width, height):
        """A constructor for the rectangle class (based on 0-rectangle.py)

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.__width = width
        self.__height = height
        
    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width
    
    
    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height
    
    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
            
    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
            
