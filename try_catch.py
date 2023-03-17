try:
    a=int(input("enter the element"))
    b=int(input("enter the second number"))
    c=a/b;
except(ZeroDivisionError):
    print("Numerator is zero")
else:
    print(c)
