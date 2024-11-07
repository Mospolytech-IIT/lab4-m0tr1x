"""This module represents funcs that described in step 3 of lab"""


def calculate_bmi(weight:int, height:int) -> float:
    """This function calculates the bmi based on the height and weight"""
    try:
        if weight <= 0:
            raise ValueError("Weight must be greater than 0")
        if height <= 0:
            raise ValueError("Height must be greater than 0")
        bmi = weight / (height ** 2)
        return bmi
    # Catching too general exception Exception [broad-exception-caught]
    # Умышленно игнорируем, потому что в задании просят общий тип исключений
    except Exception as e:
        print(f"Error in calculating BMI: {e}")
        return 0
    finally:
        print("BMI calculated, thank you for using our service")
