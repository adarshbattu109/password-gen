"""This module documents the password strength
"""

from enum import Enum, auto


class PasswordStrength(Enum):
    """Class representing the level of password strength
    """
    NOT_A_PASSWORD = auto()
    VERY_WEAK = auto()
    WEAK = auto()
    OK = auto()
    STRONG = auto()
    VERY_STRONG = auto()
    SNOWDEN = auto()


class PasswordStrenghRules:
    """Class to house rules for password strength"""
