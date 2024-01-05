#!/usr/bin/python3
# 1-rectangle.py
"""Defines rectangle class"""


class Rectangle:
    """
    A class that defines a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle with '#' characters.
        """
        if (self.__width == 0) or (self.__height == 0):
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """
        Return a string representation of the rectangle for eval().

        Returns:
            str: A string representation that can be used with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a farewell message when an instance is deleted.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
