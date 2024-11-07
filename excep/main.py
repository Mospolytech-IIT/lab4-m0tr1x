""" This is main file for running"""
import step1
import step2
import step3
import step4
import step5
import step67
import step8


def call_everything():
    """This functions calls everything"""
    print(step1.check_age(25))
    # True
    # print(step1.check_age(101))  ValueError
    print(step1.check_gender("male"))
    # print(step1.check_gender(""))  #ValueError
    print(step2.sqrt(4))  # 2
    print(step2.sqrt(-2))  # Error: Invalid number for square root None
    print(step3.calculate_bmi(80, 180))
    # 0.0024691358024691358
    # BMI calculated, thank you for using our service
    print(step3.calculate_bmi(0, 180))
    # Error in calculating BMI: Weight must be greater than 0
    # BMI calculated, thank you for using our service None
    print(step3.calculate_bmi(80, 0))
    # Error in calculating BMI: Height must be greater than 0
    # BMI calculated, thank you for using our service None
    print(step4.calculate_age("2004"))
    # Type Error
    # Thank you for using our service
    # None
    print(step4.calculate_age(2004))
    # Thank you for using our service
    # 20
    print(step4.get_photo("/Users/mtrx/Downloads/study.txt"))
    # Photo successfully uploaded True
    print(step4.get_photo(""))
    # File Not Found: [Errno 2] No such file or directory: ''
    # False
    print(step4.check_name("Grigory"))  # True
    print(step4.check_name("A"))
    # Value Error: Name must be between 2 and 25 characters
    # False
    print(step5.calculate_net_worth())
    # Value error: No arguments passed
    # None
    print(step5.calculate_net_worth(1, 2))
    # Type error: Invalid argument
    # None
    print(step5.calculate_net_worth(305.1, 302.4))  # 607.5
    print(step67.check_number(1))
    # Error: Odd number: 1
    # Проверка завершена.
    # None
    print(step67.check_number(-1))
    # Error: Negative number: -1
    # Проверка завершена.
    # None
    print(step67.check_number(2))
    # Error: Even number: 2
    # Проверка завершена.
    # None
    print(step8.percent_of_discount(100, 0))
    # ZeroDivisionError: division by zero
    # None
    print(step8.percent_of_discount(100, -1))
    # Invalid discount: Invalid discount
    # None
    print(step8.percent_of_discount(100, 50))
    # 200.0
    print(step8.get_price([1, 2]))
    # IndexError: list index out of range
    # None
    print(step8.get_price([1, 2, 3, 5, 6]))
    # 3
    print(step8.get_name())  # Grigory -> Grigory
    print(step8.get_name())  # Interrupt -> None


if __name__ == '__main__':
    call_everything()
