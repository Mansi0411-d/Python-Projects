rent=int(input("enter your flat rent="))
food=int(input("enter your food amount="))
electricity_spent=int(input("enter total electricity spent="))
charge_per_unit=int(input("enter charge per unit="))
persons=int(input("number of persons living in flat="))

total_bill=electricity_spent*charge_per_unit
output=(food+rent+total_bill)//persons
print("each person will pay=",output)