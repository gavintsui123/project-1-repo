name = input("What's your name")
name = name.strip().capitalize().title()
#attempting to switch user names with forename and surename

first,last = name.split(" ")

def greet():
    print("hello " + name)

greet()
