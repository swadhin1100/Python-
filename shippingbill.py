total_items=int(input("Enter the total items: "))
for i in range(total_items):
    i_name=input("Enter the name of item " + str(i+1) + ": ")
    item_price=float(input("Enter the price of item " + str(i+1) + ": "))
    total_price=total_items*item_price
discount=total_price*0.1
final_price=total_price-discount   
print("items are :", i_name) 
print("The total price of the items is:", total_price)
print("The discount on the total price is:", discount)
print("The final price after discount is:", final_price)