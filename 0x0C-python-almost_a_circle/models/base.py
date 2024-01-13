#!/usr/bin/python3
"""base.py"""


class Base:
    """A base class for all other classes to inherit from
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initializes Base classs with a given id and returns 

        Args:
            id (int): _description_. Defaults to None.
        """
        
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects