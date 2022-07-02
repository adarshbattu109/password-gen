"""Class to test the Password Class and associated functions
"""

import unittest
import string
from passgen.password import Password


class TestPassword(unittest.TestCase):
    """Class containing methods to test the Password class and associated functions
    """

    def test_password_length(self):
        """Method to test password generated using lower case
        """
        password_length = 10
        password_obj: Password = Password()
        password_obj.ascii_lower_case()
        actual_char_set = password_obj.generate_password(password_length)
        assert len(actual_char_set) == password_length

    def test_lower_case_password(self):
        """Method to test password generated using lower case
        """
        expected_char_set = string.ascii_lowercase
        password_length = 10
        password_obj: Password = Password()
        password_obj.ascii_lower_case()
        actual_char_set = password_obj.generate_password(password_length)
        assert set(actual_char_set) <= set(expected_char_set)

    def test_upper_case_password(self):
        """Method to test password generated using upper case
        """
        expected_char_set = string.ascii_uppercase
        password_length = 10
        password_obj: Password = Password()
        password_obj.ascii_upper_case()
        actual_char_set = password_obj.generate_password(password_length)
        assert set(actual_char_set) <= set(expected_char_set)

    def test_digit_case_password(self):
        """Method to test password generated using digits
        """
        expected_char_set = string.digits
        password_length = 10
        password_obj: Password = Password()
        password_obj.ascii_digits()
        actual_char_set = password_obj.generate_password(password_length)
        assert set(actual_char_set) <= set(expected_char_set)

    def test_symbol_case_password(self):
        """Method to test password generated using lower case
        """
        expected_char_set = string.punctuation
        password_length = 10
        password_obj: Password = Password()
        password_obj.ascii_symbols()
        actual_char_set = password_obj.generate_password(password_length)
        assert set(actual_char_set) <= set(expected_char_set)

    def test_ambigious_characters_password(self):
        """Method to test password generated using lower case
        """
        expected_char_set: str = '1lI2zZ5sS0oO'
        password_length = 10
        password_obj: Password = Password()
        password_obj.ascii_symbols()
        actual_char_set = password_obj.generate_password(password_length)
        assert set(actual_char_set).intersection(
            set(expected_char_set)) == set()


if __name__ == '__main__':
    unittest.main()
