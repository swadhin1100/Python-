nm=str(input("Enter ur name ."))
rn=str(input("Enter ur registration number ."))
c=str(input("Enter ur course name ."))
contact=int(input("Enter ur contact no. "))
t_fee=30000
khana_fee=20000
acco_fee=30000
j_fee=65000
uniform=5000
total_fee=t_fee+khana_fee+acco_fee+j_fee+uniform
scholarship_discount=0.15*total_fee
net_fee=total_fee-scholarship_discount
print("Name:", nm, "Registration Number:", rn, "Course Name:", c, "Contact No.:", contact)  
print("Total Fee:", total_fee,"Scholarship Discount:", scholarship_discount, "Net Fee:", net_fee)