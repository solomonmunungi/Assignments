

def calculator(num1,num2,num3,operator):
    if operator == '+':
        result=num1+num2+num3
    
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input('Enter third number' ))
operator = input("Enter operator (+,-,*,/): ")
print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1*num2)