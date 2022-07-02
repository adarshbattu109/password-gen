"""Module front containing the main function to generate password
"""

from passgen.password import Password
from passgen.password_strength import PasswordStrength


def main(password_length: int) -> tuple[str, PasswordStrength]:
    """Main method to trigger the password generation
    """
    password_obj = Password()
    password_obj.ascii_lower_case()
    password_obj.ascii_upper_case()
    password_obj.ascii_digits()
    password_obj.ascii_symbols()
    password_obj.remove_ambigious_characters()
    generated_password = password_obj.generate_password(password_length)
    generated_password_strength = password_obj.get_password_strength()
    return(generated_password, generated_password_strength)


if __name__ == '__main__':
    password_len: int = 10
    (password, password_strength) = main(password_len)
    print(f"Generated Password : {password}")
    print(password_strength)
