"""This module houses the class to generate a suitable password"""

import random

from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from string import punctuation

from passgen.password_strength import PasswordStrength


class Password:
    """This Class contains additive methods to generate a password
    """

    __character_set: str = ''
    __password: str = ''
    password_strength: PasswordStrength = PasswordStrength.VERY_WEAK

    def ascii_lower_case(self) -> None:
        """Method to add all lower alphabets to the password characters pool
        """
        self.__character_set += ascii_lowercase

    def ascii_upper_case(self) -> None:
        """Method to add all upper alphabets to the password characters pool
        """
        self.__character_set += ascii_uppercase

    def ascii_digits(self) -> None:
        """Method to add all digits to the password characters pool
        """
        self.__character_set += digits

    def ascii_symbols(self) -> None:
        """Method to add all lower alphabets to the password characters pool
        """
        self.__character_set += punctuation

    def remove_ambigious_characters(self) -> None:
        """Methed to eliminate ambigious characters from the password character pool
        """
        ambigious_characters: str = '1lI2zZ5sS0oO'
        self.__character_set = self.__character_set.replace(
            ambigious_characters, '')

    def calculate_password_strength(self) -> None:
        """Method to calculate password strength

        Args:
            password (str): The Generated password
        """
        pass_len: int = len(self.__password)
        if pass_len < 5:
            self.password_strength = PasswordStrength.VERY_WEAK
        elif pass_len < 6:
            self.password_strength = PasswordStrength.WEAK
        elif pass_len < 9:
            self.password_strength = PasswordStrength.OK
        elif pass_len < 14:
            self.password_strength = PasswordStrength.STRONG
        elif pass_len < 20:
            self.password_strength = PasswordStrength.VERY_STRONG
        elif pass_len > 30:
            self.password_strength = PasswordStrength.SNOWDEN

    def get_password_strength(self) -> PasswordStrength:
        """Method to get the generated password's strength
        """
        return self.password_strength

    def generate_password(self, password_length: int) -> str:
        """Method to return password as per requirements

        Args:
            password_length (int): Length of the password as requested by user

        Returns:
            str: The Generated Password
        """
        # Get a random number to seed the shuffling process
        seed_character_set = self.__character_set
        shuffle_factor: int = random.randint(0, password_length)

        for _ in range(shuffle_factor):
            self.__password = ''.join(random.sample(
                seed_character_set, password_length))

        # Generate the password strength
        self.calculate_password_strength()
        return self.__password
