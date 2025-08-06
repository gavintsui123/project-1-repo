
def giveNumber():
    return input("give a numberL ")

def operation():
    return input("give me ops (+, -, x, /, q=quit) :")

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mulitiple(x, y)
    return x * y

def div(x, y)
    return x / y


def __main__:
    x = giveNumber()
    y = giveNumber()

    result = 0
    carryon = true

    while carryon:
        op = operation()
 
        if op == '*':
            result= mulitiple(x, y)
        elif op = '+':
           result = add(x, y)

        elif op == 'q':
            carryon = false
    
        print("your result for " +op + " is : "  + result)

        

