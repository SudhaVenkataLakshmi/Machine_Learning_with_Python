a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
op = input("Enter any Operator (+,-,*,/,%): ")
if op == '+':
    print("Result is: ", a+b)
elif op == '-':
    print("Result is: ", a-b)
elif op == '*':
    print("Result is: ", a*b)
elif op == '/':
    if b != 0:
        print("Result is: ", a/b)
    else:
        print("Division by zero not allowed")
elif op == '%':
    print("Result is: ", a%b)

else:
    print("Invalid Operator!Try Again.")