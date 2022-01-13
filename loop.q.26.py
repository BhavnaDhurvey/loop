def series(a,b):
    if a>b:
        return 0
    print(a*a)
    return series (a+1,b)
a=int(input("enter the first number   "))
b=int(input("enter the last nuber   "))
print("series are  ")
series(a,b)