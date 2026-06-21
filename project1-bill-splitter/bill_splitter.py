print("=" * 40)
print("BILL SPLIT CALCULATOR".center(40))
print("=" * 40)

print("Welcome to Bill Splitter!")  #GREETINGS TO THE USER

total_bill = float(input("Enter total bill amount: $"))
tax_percentage = float(input("Enter tax percentage: "))
tip_percentage = float(input("ERnter tip percentage: "))
num_of_people = int(input("How many people: "))

tax = total_bill * (tax_percentage / 100)   #TAX CALCULATION

tip = total_bill * (tip_percentage / 100)   #TIP CALCULATION

total_amount = total_bill + tax + tip   #TOTAL AMOUNT CALCULATION

amount_per_person = total_amount / num_of_people

print("\n=" * 40)
print("CALCULATION BREAKDOWN.centre(40)")
print("=" * 40)
print(f"{'Original Bill:':<20} ${total_bill:>8.2f}")
print(f"Tax (", int(tax_percentage), "%): ${tax:>8.2f}")
print(f"Tip (", int(tip_percentage), "%): ${tip:>8.2f}")
print("-" * 40)
print(f"Total Amount: ${total_amount:>8.2f}")
print(f"Number of People: {num_of_people:>8f}")
print("-" * 40)
print(f"Each person pays: ${amount_per_person:>8.2f} /person")
print("=" * 40)