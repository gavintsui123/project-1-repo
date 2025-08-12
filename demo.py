# we want to create a program to identify odd and even

def main():
    x = int(input("What's your value for x"))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(y):
    if y / 2 == 0:
        return True

    else:
        return False

main()
