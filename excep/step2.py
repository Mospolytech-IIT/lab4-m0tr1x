"""This module represents funcs that described in step 2 of lab"""
def sqrt(number: int ) -> float:
    """This function returns the square root of a number"""
    try:
        if number < 0:
            raise ValueError("Invalid number for square root")
        return number ** 0.5
    #Catching too general exception Exception  [broad-exception-caught]
    #Умышленно игнорируем, потому что в задании просят общий тип исключений
    except Exception as e:
        print(f"Error: {e}")
        return -1
