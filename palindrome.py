#NUMBER
a=int(input("Enter a number: "))
temp=a
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("The number is not palindrome!")

#STRING
s=input("Enter a string: ")
if s==s[::-1]:
    print("The string is palindrome!")
else:
    print("The string is not palindrome!")