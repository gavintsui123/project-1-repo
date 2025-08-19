fib_dict = {}

def fib_memo(n):
    if n in fib_dict:
        return fib_dict[n]   

    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    else:
        value = fib_memo(n-1) + fib_memo(n-2)
    
    # store computed value
    fib_dict[n] = value
    return value

if __name__ == "__main__":
    print("===== Fibonacci Sequence ======")
    for i in range(1, 11):
        print(f'Fibonacci({i}) = {fib_memo(i)}')
