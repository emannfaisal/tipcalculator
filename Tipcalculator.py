print("------Welcome to the tip calculator----")

bill = float(input("What is the bill amount? "))
people = int(input("how many people? "))
tip = int(input("how much tip would you like to pay?(10,15,20) "))
percentage_tip = tip/100
tip_amount = percentage_tip*bill
total_bill = tip_amount + bill
bill_per_person = total_bill/people
print(f"Each person will pay: {bill_per_person}")
