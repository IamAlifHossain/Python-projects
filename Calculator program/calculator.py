print("Welcome to the Python Calculator!")

while True:
    num1 = float(input("Enter first number : "))
    operator = input("Enter operator (+ - * /) or (q) to quit : ")
    if operator.lower()=="q":
        print("Calculattion Done.")
        break
    else:
        num2 = float(input("Enter second number = "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Can't divide by zero")
                continue
            else:
                result = num1 / num2
        else:
            print("Invalid operator")
    print(f"The result of {num1} {operator} {num2} is : {result:.4}")
        