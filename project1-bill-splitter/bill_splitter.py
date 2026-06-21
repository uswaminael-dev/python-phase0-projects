print("========================================")
print("        BILL SPLIT CALCULATOR        ")
print("========================================")

print("Welcome to Bill Splitter!")

total_bill = float(input("Enter total bill amount: $"))
tax_percentage = float(input("Enter tax percentage: "))
tip_percentage = float(input("ERnter tip percentage: "))
num_of_people = int(input("How many people: "))

tax = total_bill * (tax_percentage / 100)

tip = total_bill * (tip_percentage / 100)


total_amount = total_bill + tax + tip

amount_per_person = total_amount / num_of_people

print("\n========================================")
print("         CALCULATION BREAKDOWN        ")
print("========================================")
print("Orignal Bill: $", total_bill)
print("Tax (", int(tax_percentage), "%): $" , tax_percentage)
print("Tip (", int(tip_percentage), "%): $" , tip_percentage)
print("----------------------------------------")
print("Total Amount: $", total_amount)
print("Number of People: " , num_of_people)
print("----------------------------------------")
print(f"Each person pays: ${amount_per_person:.2f}")
print("========================================")