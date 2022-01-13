sum=0.0
nocount=0
while True:     
    number=float(input("enter the number:"))
    sum+=number
    nocount+=1

    choice= input("add another number?(y/n):")
    if choice.casefold()=="n":
        break

average=sum/nocount

print(float,"sum:{sum}")
print(float,"average:{average}")
        