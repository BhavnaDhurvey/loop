p=int(input("enter the number...."))
i=1
sum=0
while i<=p:
    if i%2!=0:
        print(i)
        sum=sum+i
    i=i+1
print("=",sum)