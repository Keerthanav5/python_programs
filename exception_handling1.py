try:
    a=int(input("Enter the first num:"))
    b=int(input("Enter the second num:"))
    c=a/b
except ZeroDivisionError:
    print("Cant divide by zero")
