n=20
t=True
for i in range (2,n):
    if n%i==0:
        t=False
        print("not")
        break
    if t:
        print("prime")

