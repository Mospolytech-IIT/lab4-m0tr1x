"""This module represents funcs that described in step 1 of lab"""

def check_age(age: int) -> bool:
    """This function checks if the age valid for our goals"""
    if age < 0 or age > 100:
        raise ValueError("Invalid age")
    return True

def check_gender(gender: str) -> bool:
    """This function checks if the gender valid for our goals"""
    if gender not in ["male", "female"]:
        raise ValueError("Invalid gender")
    if gender == "male":
        return True
    return False
