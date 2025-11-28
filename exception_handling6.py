try:
    f=open("dat.txt","r")
    data=f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("Something went wrong")
finally:
    print("File closed")
    
