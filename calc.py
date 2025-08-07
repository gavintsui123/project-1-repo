def calculate(x ,y , operator ):
    if operator == "+":
        return x + y

    elif operator == "-":
        return x - y
    
    elif operator == "*":
        return x * y

    elif operator == "/":
        if y == 0: 
            print("invalid answer")
        else:
            return x / y

x = float(int(input("What's your value for x ")))
y = float(int(input("What's your value for y ")))
operator = input("enter and operation + , - , * , / ")

result = calculate(x,y, operator)

print(result)


    
        