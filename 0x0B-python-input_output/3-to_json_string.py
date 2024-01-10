#!/usr/bin/python3

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Parameters:
    - my_obj: Any object

    Returns:
    - JSON representation as a string
    """
    return json.dumps(my_obj)
