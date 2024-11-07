"""This module represents funcs that described in step 8 of lab"""

def percent_of_discount(price:float, discount:float)-> float:
    """This function is used to calculate origin price"""
    try:
        if discount < 0:
            raise ValueError("Invalid discount")
        original_price = price * price / discount
        return original_price
    except ValueError as e:
        print(f"Invalid discount: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return None

def get_name() -> str:
    """This function is used to get name from user"""
    try:
        name = str(input(""))
        return name
    except KeyboardInterrupt as e:
        print(f"User interrupted {e}")
        return None

def get_price(array: list) -> float:
    """This function is used to find price of the third element in array"""
    try:
        price = array[2]
        return price
    except IndexError as e:
        print(f"IndexError: {e}")
        return None
