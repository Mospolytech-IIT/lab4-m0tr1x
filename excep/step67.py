"""This module represents funcs that described in step 6 and 7 of lab"""
class NegativeException(ValueError):
    """This class represents negative number exception"""
    def __init__(self, message):
        super().__init__(message)


class EvenException(ValueError):
    """This class represents even number exception"""
    def __init__(self, message):
        super().__init__(message)


class OddException(ValueError):
    """This class represents odd number exception"""
    def __init__(self, message):
        super().__init__(message)


def check_number(number:int):
    """This function checks if number is positive"""
    try:
        if number < 0:
            raise NegativeException(f"Negative number: {number}")
        if number % 2 == 0:
            raise EvenException(f"Even number: {number}")
        if number % 2 != 0:
            raise OddException(f"Odd number: {number}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Проверка завершена.")
