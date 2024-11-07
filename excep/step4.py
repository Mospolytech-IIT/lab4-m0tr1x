"""This module represents funcs that described in step 4 of lab"""
from datetime import datetime

def calculate_age(birth_year) -> int:
    """This function calculates the age of a given person"""
    try:
        current_year = datetime.now().year
        if not isinstance(birth_year, int):
            raise TypeError
        age = current_year - birth_year
        return age
    except TypeError as e:
        print(f"Type Error {e}")
        return None
    finally:
        print("Thank you for using our service")


def check_name(name: str) -> bool:
    """This function check if the name is valid for us"""
    try:
        if len(name) <= 1 or len(name) > 25:
            raise ValueError("Name must be between 2 and 25 characters")
        return True
    except ValueError as e:
        print(f"Value Error: {e}")
        return False

def get_photo(path:str) -> bool:
    """This function gets the photo from the user"""
    try:
        with open(path, 'r', encoding='utf-8'):
            print("Photo successfully uploaded")
            return True
    except FileNotFoundError as e:
        print(f"File Not Found: {e}")
        return False
