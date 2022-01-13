a=int(input("enter the number,,,,,,,,,"))
num=5
i=1
while i<=a:
    if a<num:
        print("number enter by you entered is small, try one more time ")
    if a>num:
        print("number entered by you entered is greater,try one more time")
    elif a==num:
        print("wow you guessed correct number")
    # else:
        # print("guessing until all the chances are filled")
    break
    i=i+1