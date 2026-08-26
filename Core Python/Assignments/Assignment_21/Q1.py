# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.


class Calculator:
    def calculator(self):
        operator = input("Enter operator (+, -, *, /): ")

        try :
            num1=int(input('Enter number1:'))
            num2=int(input('Enter number2:'))
            operator=input('Enter operator:')
            if operator not in ['+','-','*','/']:
                raise('This operator is not allowed')
            if operator=='+':
                print(num1+num2)
            elif operator=='-':
                print(num1-num2)
            elif operator=='*':
                print(num1*num2)
            elif operator=='/':
                print(num1/num2)
            else:
                print('invalide operator')
        except Exception as e:
            if str(e) == "Invalid operator":
                print("Error: Invalid operator entered.")
            else:
                print("Error: Cannot divide by zero.")

c=Calculator()
c.calculator()