#!/usr/bin/python3
# 1-rectangle.py
"""Defines rectangle class"""


class Rectangle:
    """A rectangle class (based on 0-rectangle.py)

    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialises a new Rectangle with given width and height

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle

        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value (int): the new width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle

        Args:
            value (int): the new height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
