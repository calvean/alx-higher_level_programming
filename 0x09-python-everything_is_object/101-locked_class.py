#!/usr/bin/python3
class LockedClass:
    """Prevent the user from instantiating new attributes
    other than attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
