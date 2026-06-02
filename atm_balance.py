total_ammount=float(input("Enter the total ammount in your account: "))
withdraw_ammount=float(input("Enter the ammount you want to withdraw: "))
if withdraw_ammount>total_ammount:
    print("Lee...gareeeeeb tera bap chhodke gya ya teri maa..(insufficient balance).")
    print( total_ammount,"yeh leee gareeeeb... itna hi hai")
elif withdraw_ammount==total_ammount:
    print("withdraw successful... but your account is now empty.")
else:
    remaining_balance=total_ammount-withdraw_ammount
    print("withdraw successful... your remaining balance is:", remaining_balance)