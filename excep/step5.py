"""This module represents funcs that described in step 5 of lab"""

def calculate_net_worth(*args):
    """This function calculates net worth based on args passed"""
    try:
        if not args:
            raise ValueError("No arguments passed")
        total = 0
        for arg in args:
            if not isinstance(arg,float):
                raise TypeError("Invalid argument")
            total += arg
        return total
    except ValueError as e:
        print(f"Value error: {e}")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
