#!/usr/bin/python3
"""Module conatining a class that blocks dynamic attribute creation"""

class LockedClass():
    """locked class"""
    __slots__ = ['first_name']
