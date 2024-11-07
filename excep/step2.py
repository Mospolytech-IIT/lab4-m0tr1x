"""This module represents funcs that described in step 2 of lab"""
def sqrt(number: int ) -> float:
    """This function returns the square root of a number"""
    try:
        if number < 0:
            raise ValueError("Число не может быть отрицательным")
        return number ** 0.5
    #Catching too general exception Exception (8:11) [broad-exception-caught]
    #Умышленно игнорируем, потому что в задании просят общий тип исключений
    except Exception as e:
        print(f"Ошибка: {e}")
        return -1
