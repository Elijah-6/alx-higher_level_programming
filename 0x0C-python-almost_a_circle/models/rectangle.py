#!usr/bin/python3
"""Rectangle class"""
from .base import Base

class Rectangle(Base):
    """
    A class representing a rectangle, inheriting from the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The identifier of the rectangle, inherited from the Base class.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a new Rectangle instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner of the rectangle. Default is 0.
            y (int): The y-coordinate of the top-left corner of the rectangle. Default is 0.
            id (int): The identifier of the rectangle, inherited from the Base class. Default is None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
        @property
        def width(self):
            """int: The width of the rectangle."""
            return self.__width
        
        @width.setter
        def width(self, value):
            """
            Set the width of the rectangle.

            Parameters:
                value (int): The new width value.
        """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        
        @property
        def height(self):
            """ int: The height of the rectangle."""
            return self.__height
        
        @height.setter
        def height(self, value):
            """
            Set the height of the rectangle.

            Parameters:
                value (int): The new height value.
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__height = value
            
        @property
        def x(self):
            """int: The x-coordinate of the top-left corner of the rectangle."""
            return self.__x

        @x.setter
        def x(self, value):
            """
            Set the x-coordinate of the top-left corner of the rectangle.

            Parameters:
            value (int): The new x-coordinate value.
            """
            if not isinstance(value,int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__x = value

        @property
        def y(self):
            """int: The y-coordinate of the top-left corner of the rectangle."""
            return self.__y

        @y.setter
        def y(self, value):
            """
            Set the y-coordinate of the top-left corner of the rectangle.

            Parameters:
            value (int): The new y-coordinate value.
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__y = value