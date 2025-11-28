f=None
try:
    f=open("data.txt","r")
    data=f.read()
    print(data)
except FileNotFoundError:
    print("Something went wrong")
finally:
    if f is not None and not f.closed:
        f.close()
