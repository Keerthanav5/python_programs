try:
    a=int(input("Enter first num:"))
    b=int(input("Enter second num:"))
    c=a/b
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cant divide by zero")
