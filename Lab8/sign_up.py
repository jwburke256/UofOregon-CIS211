"""
CIS 211 Spring 2021 Week 8 Lab 8

Author: Jacob Burke

Credits: N/A

Created a set of functions to demonstrate proficiency with using
regular expressions in python. The functions check a string
to see if it matches a given search pattern, in order to
match email and password creation criteria.
"""
import re


def validate_email(email: str) -> bool:
    """The program first prompts the user for an email address which will serve as the username.
    The requirements for acceptable email addresses are as follows:
    - Cannot start with a digit.
    - Should only contain one @ symbol delimiting the username from the domain.
    - Only accepted domains should end with '.edu' or '.com'.
    """
    x = re.match(r"\D[^@]+@{1}[^@]+((\.edu)|(\.com))$", email)
    if x:
        return True
    return False


def validate_password(pw) -> bool:
    """Once the email has been validated, the program should ask the user for a password.
    The requirements for an acceptable password are as follows:
    - Must contain at least 10 characters
    - Must contain at least 1 digit
    - Must contain at least one special symbol (non-alphanumeric)
    """
    x = re.match("(.*\d.*\W.*)|(.*\W.*\d.*)", pw)
    if x and len(pw) >= 10:
        return True
    return False


def main():
    email = False
    while not email:
        email = validate_email(input("Provide an email address: "))
        while not email:
            email = validate_email(input("Invalid email, provide a different one: "))

    password = False
    while not password:
        password = validate_password(input("Input your password: "))
        while not password:
            password = validate_password(input("Invalid password, provide a different one: "))
    print("Sign Up Successful")

if __name__ == "__main__":
    main()

    """
    string1 = "123@gmail.com"  # starts with a digit
    string2 = "asdf@@gmail.com"  # has multiple @ symbols
    string3 = "oregonduck@uo.edu"  # True, fits criteria
    string4 = "oregonduck@uo.org"  # does not end with .com or .edu
    print(validate_email(string1))
    print(validate_email(string2))
    print(validate_email(string3))
    print(validate_email(string4))


    pw1 = "1234@"
    pw2 = "asdfghjkliop@"
    pw3 = "1234567890"
    pw4 = "asdf1234$ghj"
    print(validate_password(pw1)) # less than 10 characters
    print(validate_password(pw2)) # no digits
    print(validate_password(pw3)) # no special characters
    print(validate_password(pw4)) # True, fits criteria
    """
