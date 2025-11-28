try:
    a=int(input("Enter a first num:"))
    b=int(input("Enter a second num:"))
    c=a/b
except ZeroDivisionError:
    print("Cant divide by zero")
else:
    print("Successful division")
