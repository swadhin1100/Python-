num=int(input("enter a number: "))
factorial=1
if num <0:
    print ("factorial doesnot exist negtive number")
else:
    for i in range (1,num+1):
        factorial=factorial*1
        print("factorial of",num,
              "is",factorial)