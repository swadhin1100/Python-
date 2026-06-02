total_members = int(input("Members in a room: "))
rent=5000
electricity_bill=1000
water_bill=300
total_bill=rent+electricity_bill+water_bill
bill_per_person=total_bill/total_members
print("Each person has to pay:", bill_per_person)