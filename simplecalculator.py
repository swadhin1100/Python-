a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
choice=input("Enter the operation you want to perform (+, -, *, /): ")
if choice=='+':
    print("The result is: ", a+b)
elif choice=='-':   
    print("The result is: ", a-b)
elif choice=='*':
    print("The result is: ", a*b)
elif choice=='/':
    if b!=0:
        print("The result is: ", a/b)
    else:
        print("entered invalid input")