"""This module represents funcs that described in step 2 of lab"""
def sqrt(number: int ) -> float:
    """This function returns the square root of a number"""
    try:
        if number < 0:
            raise Exception("Invalid number for square root")
        return number ** 0.5
    #Catching too general exception Exception  [broad-exception-caught]
    #Raising too general exception: Exception (10:12) [broad-exception-raised]
    #Умышленно игнорируем, потому что в задании просят общий тип исключений
    except Exception as e:
        print(f"Error: {e}")
        return None
