#!/usr/bin/python3
"""This defines a locked class"""


class LockedClass:
    """Allows instantiaion of attribute 'first_name' and nothing else"""
    __slots__ = ["first_name"]
