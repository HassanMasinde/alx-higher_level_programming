#!/usr/bin/python3
"""defines  object attribute and methods using lookup function."""


def lookup(obj):
    """return a list of object's available attributes and methods."""
    return (dir(obj))
